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
    original_table = table
    if table.startswith("tbl"):
        table = table.split("tbl")[1]
    # Capitalize table name
    table = table[0].upper() + table[1:]

    return table, original_table


def get_fields(keywords, table):
    result = {}

    for keyword in keywords:
        try:
            keyword = keyword.strip()

            field = re.findall(r'\`(.*?)\`', keyword)[0]
            # Store initial field name before altering it for the lookup in the repository class
            field_backup = field
            fields_split = keyword.split(field)[1]
            datatype = re.findall(r'\w+', fields_split[2:])[0]
            limits = re.findall(r'\((.*?)\)', fields_split)
            not_null = True if "not null" in keyword.lower() else False

            # avoid Python keyword clashes
            if field.lower() == "type":
                field = "type_%s" % table
            elif field.lower() == "id":
                field = "%s_id" % table
            elif field.lower() == "property":
                field = "%s_property" % table

            result[field.lower()] = {
                "datatype": datatype,
                "not_null": not_null,
                "limits": limits,
                "real_name": field_backup,
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
        table, original_table = get_table_name(re.findall(r'\`(.*?)\`', d))
        fields = get_fields("(".join(d.split("(")[1:]).split(", "), table)

        fields.update({
            "original_table_name": original_table
        })

        result[table] = fields

    return result


def get_database_name(data):
    try:
        database_name = re.findall(r'CREATE +DATABASE +IF +NOT +EXISTS +`\w+`', data)[0]
        database_name = re.findall(r'`\w+`', database_name)[0][1:-1]
    except Exception:
        database_name = "unknown database"

    return database_name


def check_int_limits(limits, tabs):
    limits = limits[0].split(",")

    if len(limits) == 2:
        min_value = int(limits[0])
        max_value = int(limits[1])

        return "\t" * tabs + "if %d < value < %d:" % (min_value, max_value)
    elif len(limits) == 1:
        return "\t" * tabs + "if len(str(value)) == %d:" % limits[0]
    else:
        return "# ## FAILED TO VERIFY INT LIMITS: %s" % limits


def check_decimal_limits(limits, tabs):
    limits_split = limits[0].split(",")
    if len(limits_split) == 0:
        limits_split.append("0")
    max_after_comma = int(limits_split[1])
    max_before_comma = int(limits_split[0]) - max_after_comma

    result = "\t" * tabs + "if \".\" in str(value):"
    result += "\n" + "\t" * (tabs + 1) + \
              "if ((len(str(value).split(\".\")[0]) <= %d) and (len(str(value).split(\".\")[1]) <= %d)):" % (
                  max_before_comma, max_after_comma
              )

    return result


def check_limits(lines, limits, tabs, prop, datatype, exact=False):
    if limits:
        if datatype == "str":
            limit = limits[0]
            try:
                limit = int(limit)
                if exact:
                    lines.append("\t" * tabs + "if len(str(value)) == %d:" % limit)
                else:
                    lines.append("\t" * tabs + "if len(str(value)) <= %d:" % limit)
                lines.append("\t" * (tabs + 1) + "self._%s = str(value)" % prop)
                lines.append("\t" * tabs + "else:")
                if exact:
                    lines.append("\t" * (tabs + 1) +
                                 "self._valueErrors[\"%s\"] = "
                                 "ValueError(\"input voor %s is niet de juitse lengte (%s)\")"
                                 % (prop, prop, limit))
                else:
                    lines.append(
                        "\t" * (tabs + 1) + "self._valueErrors[\"%s\"] = ValueError(\"input voor %s is te lang\")" % (
                            prop, prop
                        ))
            except Exception:
                # Limit cant be turned into an int, so it's a regular expression
                lines.append("\t" * tabs + "if len(re.findall(r'%s', value)[0]) == len(value):" % limit)
                lines.append("\t" * (tabs + 1) + "self._%s = str(value)" % prop)
                lines.append("\t" * tabs + "else:")
                lines.append("\t" * (tabs + 1) +
                             "self._valueErrors[\"%s\"] = "
                             "ValueError(\"input voor %s match het patroon niet (%s)\")"
                             % (prop, prop, limit))
        else:
            if datatype == "int":
                lines.append(check_int_limits(limits, tabs))
                # One less indent bcus with floats we need to verify the "."
                tabs -= 1
            elif datatype == "float":
                lines.append(check_decimal_limits(limits, tabs))

            lines.append("\t" * (tabs + 2) + "self._%s = value" % prop)
            lines.append("\t" * (tabs + 1) + "else:")
            lines.append("\t" * (tabs + 2) +
                         "self._valueErrors[\"%s\"] = ValueError(\"input voor %s is te groot / klein\")" % (
                             prop, prop
                         ))

            if datatype == "float":
                lines.append("\t" * tabs + "else:")
                lines.append("\t" * (tabs + 1) + "if len(str(value)) <= %s:" % limits[0].split(",")[0])
                lines.append("\t" * (tabs + 2) + "self._%s = value" % prop)
                lines.append("\t" * (tabs + 1) + "else:")
                lines.append(
                    "\t" * (tabs + 2) + "self._valueErrors[\"%s\"] = ValueError(\"input voor %s is te lang\")" % (
                        prop, prop
                    ))
    else:
        lines.append("\t" * tabs + "self._%s = str(value)" % prop)

    return lines


def translate_datatype(tabs, lines, limits, datatype):
    exact = False

    if datatype == "varchar" or datatype == "longtext":
        datatype = "str"

    elif datatype == "char":
        exact = True
        datatype = "str"

    elif datatype == "decimal" or datatype == "double":
        datatype = "float"

    elif datatype == "tinyint":
        lines.append("\t" * tabs + "# tinyint")
        datatype = "int"
        limits = ['-128,127']

    elif datatype == "smallint":
        lines.append("\t" * tabs + "# smallint")
        datatype = "int"
        limits = ['-32768,32767']

    elif datatype == "mediumint":
        lines.append("\t" * tabs + "# mediumint")
        datatype = "int"
        limits = ['-8388608,8388607']

    elif datatype == "int" or datatype == "integer":
        lines.append("\t" * tabs + "# regular int")
        datatype = "int"
        limits = ['-2147483648,2147483647']

    elif datatype == "datetime" or datatype == "timestamp":
        lines.append("\t" * tabs + "#'0000-00-00 00:00:00'")
        datatype = "str"
        limits = [r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"]
        exact = True

    elif datatype == "time":
        lines.append("\t" * tabs + "#'00:00:00'")
        datatype = "str"
        limits = [r"\d{2}:\d{2}:\d{2}"]
        exact = True

    elif datatype == "date":
        lines.append("\t" * tabs + "#'0000-00-00'")
        datatype = "str"
        limits = [r"\d{4}-\d{2}-\d{2}"]
        exact = True

    elif datatype == "year":
        lines.append("\t" * tabs + "#'0000'")
        datatype = "str"
        limits = [r"\d{4}"]
        exact = True

    return exact, lines, limits, datatype


def check_datatype(lines, datatype, prop, tabs, limits=None):
    # Exact match of the limits or <=
    exact, lines, limits, datatype = translate_datatype(tabs, lines, limits, datatype)

    lines.append("\t" * tabs + "if type(value) is %s:" % datatype)
    lines = check_limits(lines, limits, tabs + 1, prop, datatype, exact)

    lines.append("\t" * tabs + "else:")
    lines.append("\t" * (tabs + 1) + "self._valueErrors[\"%s\"] = ValueError(\"input voor %s is ongeldig\")" % (
        prop, prop
    ))

    return lines


def generate_repositories(repos, database_name, tables):
    for table in tables.keys():
        lines = [
            "from models.%s import %s" % (table, table),
            "from repositories.Database import Database",
            "",
            "",
            "class %sRepository:" % table,
            "\t@ staticmethod",
            "\tdef read_all():",
            "\t\tresult = []",
            "\t\tsql = \"SELECT * FROM %s.%s\"" % (database_name, tables[table]["original_table_name"]),
            "\t\trows = Database.get_rows(sql)",
            "",
            "\t\tif rows is not None:",
            "\t\t\tfor row in rows:",
            "\t\t\t\t# mapping naar object",
            "\t\t\t\tresult.append(%sRepository.map_to_object(row))" % table,
            "",
            "\t\treturn result",
            "",
            "\t@staticmethod",
            "\tdef read_single(_id):",
            "\t\tif not _id:",
            "\t\t\treturn \"Ongedlig ID. Probeer opnieuw\"",
            "",
            "\t\tsql = \"\"\"",
            "\t\tSELECT",
            "\t\t\t*",
            "\t\tFROM %s.%s" % (database_name, tables[table]["original_table_name"]),
            "\t\tWHERE %s = %%s" % list(tables[table].keys())[0],
            "\t\t\"\"\"",
            "\t\tparams = [_id]",
            "",
            "\t\tresult = Database.get_one_row(sql, params)",
            "",
            "\t\tif type(result) is dict:",
            "\t\t\t# Mapping naar %s object" % table,
            "\t\t\t result = %sRepository.map_to_object(result)" % table,
            "",
            "\t\treturn result",
            "",
            "\t@staticmethod",
            "\tdef check_column(row, column_name):",
            "\t\tresult = None",
            "\t\tif column_name in row.keys() and row[column_name] is not None:",
            "\t\t\tresult = row[column_name]",
            "",
            "\t\treturn result",
            "",
            "\t@staticmethod",
            "\tdef map_to_object(row):",
            "\t\tif row is not None and type(row) is dict:"
        ]

        real_properties = [tables[table][p]["real_name"] for p in tables[table].keys() if p != "original_table_name"]
        rewritten_properties = [p for p in tables[table].keys() if p != "original_table_name"]

        for prop, rewritten_prop in zip(real_properties, rewritten_properties):
            _, _, _, datatype = translate_datatype(
                0, [], [], tables[table][rewritten_prop]["datatype"]
            )

            lines.append("\t\t\t%s = %sRepository.check_column(row, \"%s\")" % (
                rewritten_prop, table, prop
            ))

            if datatype != "str":
                # Convert if possible
                lines.append("\t\t\t%s = %s(%s) if %s is not None else None" % (
                    rewritten_prop, datatype, rewritten_prop, rewritten_prop
                ))
                lines.append("")

        lines.append("")
        lines.append("\t\treturn %s(%s)" % (
            table, ", ".join(rewritten_properties)
        ))

        with open(os.path.join(repos, "%sRepository" % table) + ".py", "w") as f:
            f.writelines(["%s\n" % line for line in lines])


def generate_classes(models, tables):
    print(tables)
    for table in tables.keys():
        lines = [
            "import re",
            "",
            "",
            "class %s:" % table
        ]

        properties = [
            prop.lower() for prop in tables[table].keys()
            if prop != "original_table_name"
        ]

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
            datatype = tables[table][prop]["datatype"].lower()

            lines.append("\n\t@property")
            lines.append("\tdef %s(self):" % prop)
            lines.append("\t\treturn self._%s" % prop)
            lines.append("\t@%s.setter" % prop)
            lines.append("\tdef %s(self, value):" % prop)
            if not_null:
                # This property CAN NOT be None
                lines.append("\t\t# Property CAN NOT be None")
                lines = check_datatype(lines, datatype, prop, tabs=2, limits=limits)
            else:
                # This property CAN be None
                lines.append("\t\t# Property CAN be None")
                lines.append("\t\tif value is None:")
                lines.append("\t\t\tself._%s = value" % prop)
                lines.append("\t\telse:")
                lines = check_datatype(lines, datatype, prop, tabs=3, limits=limits)

        lines.append("\n\tdef __str__(self):")
        lines.append("\t\treturn \"%s: %s: %%s\" %% self.%s" % (table, properties[0], properties[0]))

        lines.append("\n\tdef __repr__(self):")
        lines.append("\t\tself.__str__()")

        with open(os.path.join(models, table) + ".py", "w") as f:
            f.writelines(["%s\n" % line for line in lines])


def convert_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read().replace('\n', ' ').replace('\r', '')

    database_name = get_database_name(data)
    tables = get_database_tables(data)

    root_dir = os.path.join(os.path.dirname(filepath), "%s_python" % database_name)
    models_dir = os.path.join(root_dir, "models")
    repositories_dir = os.path.join(root_dir, "repositories")

    # Clear previous exports
    if os.path.exists(root_dir):
        try:
            shutil.rmtree(root_dir, True)
        except Exception:
            pass

    os.mkdir(root_dir)
    os.mkdir(models_dir)
    os.mkdir(repositories_dir)

    generate_classes(models_dir, tables)
    generate_repositories(repositories_dir, database_name, tables)


def main():
    sql_files = get_sql_files()
    for f in sql_files:
        convert_file(f)


if __name__ == '__main__':
    import os
    import re
    import shutil

    main()
