def get_sql_files():
    # maybe add a browser dialog here
    search_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sql")

    return [
        os.path.join(search_directory, f) for f in
        os.listdir(search_directory)
        if os.path.splitext(f)[1] == ".sql"
    ]


def get_table_name(keywords):
    table = keywords[0]
    if table.startswith("tbl"):
        table = table.split("tbl")[1]
    # Capitalize table name
    table = table[0].upper() + table[1:]

    return table


def get_fields(keywords, table):
    result = {}

    for keyword in keywords:
        try:
            keyword = keyword.strip()
            # print(keyword)
            field = re.findall(r'\`(.*?)\`', keyword)[0]
            fields_split = keyword.split(field)[1]
            datatype = re.findall(r'\w+', fields_split[2:])[0]
            limits = re.findall(r'\((.*?)\)', fields_split)
            not_null = True if "not null" in keyword.lower() else False

            # avoid Python keyword clashes
            if field.lower() == "type":
                field = "%s_type" % table
            elif field.lower() == "id":
                field = "%s_id" % table
            elif field.lower() == "property":
                field = "%s_property" % table

            result[field.lower()] = {
                "datatype": datatype,
                "not_null": not_null,
                "limits": limits
            }
        except Exception:
            pass

    return result


def get_database_tables(data):
    result = dict()

    # Split per table and remove the first
    split_data = data.split("CREATE TABLE ")[1:]
    for d in split_data:
        # Strip out the access data
        d = d.split("ENGINE")[0].split("KEY")[0]

        # Extract words between ``
        table = get_table_name(re.findall(r'\`(.*?)\`', d))
        fields = get_fields("(".join(d.split("(")[1:]).split(", "), table)

        result[table] = fields

    return result


def get_database_name(data):
    try:
        database_name = re.findall(r'CREATE +DATABASE +IF +NOT +EXISTS +`\w+`', data)[0]
        database_name = re.findall(r'`\w+`', database_name)[0][1:-1]
    except Exception:
        database_name = "unknown database"

    return database_name


def check_decimal_limits(limits):
    limits_split = limits[0].split(",")
    max_after_comma = int(limits_split[1])
    max_before_comma = int(limits_split[0]) - max_after_comma

    result = "\t\t\tif \".\" in str(value):"
    result += "\n\t\t\t\tif ((len(str(value).split(\".\")[0]) <= %d) and (len(str(value).split(\".\")[1]) <= %d)):" % (
            max_before_comma, max_after_comma
        )

    return result


def generate_classes(models, tables):
    print(tables)
    for table in tables.keys():
        lines = ["class %s:" % table]

        properties = [prop.lower() for prop in tables[table].keys()]

        lines.append("\tdef __init__(self, %s):" % ", ".join(properties))
        lines.append("\t\tself._valueErrors = dict()")
        for prop in properties:
            lines.append("\t\tself.%s = %s" % (prop, prop))

        lines.append("\n\t@property")
        lines.append("\tdef valueErrors(self):")
        lines.append("\t\treturn self._valueErrors")

        lines.append("\n\t@property")
        lines.append("\tdef isValid(self):")
        lines.append("\t\treturn len(self._valueErrors) == 0")

        for prop in properties:
            limits = tables[table][prop]["limits"]
            not_null = tables[table][prop]["not_null"]
            datatype = tables[table][prop]["datatype"]

            lines.append("\n\t@property")
            lines.append("\tdef %s(self):" % prop)
            lines.append("\t\treturn self._%s" % prop)
            lines.append("\t@%s.setter" % prop)
            lines.append("\tdef %s(self, value):" % prop)
            if not_null:
                # This property CAN NOT be None
                if datatype == "int":
                    lines.append("\t\tif type(value) is int:")
                    lines.append("\t\t\tself._%s = value" % prop)
                    lines.append("\t\telse:")
                    lines.append("\t\t\tself._valueErrors[\"%s\"] = ValueError(\"input voor %s is ongeldig\")" % (
                        prop, prop
                    ))
                elif datatype == "decimal":
                    lines.append("\t\tif type(value) is float:")
                    if limits:
                        lines.append(check_decimal_limits(limits))
                        lines.append("\t\t\t\t\tself._%s = value" % prop)
                        lines.append("\t\t\t\telse:")
                        lines.append("\t\t\t\t\tself._valueErrors[\"%s\"] = ValueError(\"input voor %s is te lang\")" % (
                            prop, prop
                        ))
                        lines.append("\t\t\telse:")
                        lines.append("\t\t\t\tif len(str(value)) <= %s:" % limits[0].split(",")[0])
                        lines.append("\t\t\t\t\tself._%s = value" % prop)
                        lines.append("\t\t\t\telse:")
                        lines.append("\t\t\t\t\tself._valueErrors[\"%s\"] = ValueError(\"input voor %s is te lang\")" % (
                            prop, prop
                        ))
                    else:
                        lines.append("\t\tself._%s = value" % prop)
                elif datatype == "varchar":
                    lines.append("\t\tif type(value) is str:")
                    if limits:
                        lines.append("\t\t\tif len(value) <= %s:" % limits[0])
                        lines.append("\t\t\t\tself._%s = value" % prop)
                        lines.append("\t\t\telse:")
                        lines.append("\t\t\t\tself._valueErrors[\"%s\"] = ValueError(\"input voor %s is te lang\")" % (
                            prop, prop
                        ))
                    else:
                        lines.append("\t\t\tself._%s = value" % prop)
                    lines.append("\t\telse:")
                    lines.append("\t\t\tself._valueErrors[\"%s\"] = ValueError(\"input voor %s is ongeldig\")" % (
                        prop, prop
                    ))
                elif datatype == "tinyint":
                    print("https://dev.mysql.com/doc/refman/8.0/en/integer-types.html")
                else:
                    print(datatype, "not yet supported")
            else:
                # This property CAN be None
                lines.append("\t\tif value is None:")
                lines.append("\t\t\tself._%s = value" % prop)
                lines.append("\t\telse:")
                # TODO opsplitsen in functies en dan eventueel "\t"+return value doen hier
                if limits:
                    try:
                        limit = int(limits[0])
                        lines.append("\t\t\tif len(str(value)) <= %d:" % limit)
                        lines.append("\t\t\t\tself._%s = str(value)" % prop)
                        lines.append("\t\t\telse:")
                        lines.append("\t\t\t\tself._valueErrors[\"%s\"] = ValueError(\"input voor %s is te lang\")" % (
                            prop, prop
                        ))
                    except Exception:
                        lines.append(check_decimal_limits(limits))
                        lines.append("\t\t\t\t\tself._%s = value" % prop)
                        lines.append("\t\t\t\telse:")
                        lines.append("\t\t\t\t\tself._valueErrors[\"%s\"] = ValueError(\"input voor %s is te lang\")" % (
                            prop, prop
                        ))
                        lines.append("\t\t\telse:")
                        lines.append("\t\t\t\tif len(str(value)) <= %s:" % limits[0].split(",")[0])
                        lines.append("\t\t\t\t\tself._%s = value" % prop)
                        lines.append("\t\t\t\telse:")
                        lines.append("\t\t\t\t\tself._valueErrors[\"%s\"] = ValueError(\"input voor %s is te lang\")" % (
                            prop, prop
                        ))
                else:
                    lines.append("\t\t\tself._%s = str(value)" % prop)

        lines.append("\n\tdef __str__(self):")
        lines.append("\t\treturn \"%s: %s: %%s\" %% self.%s" % (table, properties[0], properties[0]))

        lines.append("\n\tdef __repr__(self):")
        lines.append("\t\tself.__str__()")

        with open(os.path.join(models, table)+".py", "w") as f:
            f.writelines(["%s\n" % line for line in lines])


def convert_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read().replace('\n', ' ').replace('\r', '')

    database_name = get_database_name(data)
    tables = get_database_tables(data)

    models_dir = os.path.join(os.path.dirname(filepath), "%s_models" % database_name)
    # Clear previous exports
    if os.path.exists(models_dir):
        try:
            shutil.rmtree(models_dir, True)
        except Exception:
            pass

    os.mkdir(models_dir)
    generate_classes(models_dir, tables)


def main():
    sql_files = get_sql_files()
    for f in sql_files:
        convert_file(f)


if __name__ == '__main__':
    import os
    import re
    import shutil

    main()
