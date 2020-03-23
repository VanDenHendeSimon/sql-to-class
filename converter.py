def get_sql_files():
    """
    This function will list all .sql files in the sql folder.
    A possible extension to the script could be browsing for .sql files.
    However, this way works fine for the purposes that I intend to use it for

    :return: list of all .sql files within the sql directory, located in the root of this project
    """
    # maybe add a browser dialog here
    search_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sql")

    return [
        os.path.join(search_directory, f) for f in
        os.listdir(search_directory)
        if os.path.splitext(f)[1] == ".sql"
    ]


def get_table_name(keywords):
    """
    This function will extract the name of the current table and alter it
    This altering includes capitalising the first letter and extracting a possible 'tbl' prefix

    :param keywords: a list of words between backticks in this table's part of the .sql file
    :return: altered name of the table, as well as the original name
    This original name is used in the repository classes to generate the MySQL queries.
    """
    table = keywords[0]
    original_table = table
    if table.startswith("tbl"):
        table = table.split("tbl")[1]
    # Capitalize table name
    table = table[0].upper() + table[1:]

    return table, original_table


def get_fields(keywords, table):
    """
    This function will store all of the columns of this database in a dictionary

    :param keywords: a list of words between backticks in this table's part of the .sql file
    :param table: the name of the current table, used to deform clashing names like 'id' and 'type'
    :return: a dictionary that contains all columns that belong to the current table
    as well as the data that is needed to reconstruct said column as a Python class
    """
    result = {}

    for keyword in keywords:
        try:
            keyword = keyword.strip()

            field = re.findall(r'\`(.*?)\`', keyword)[0]
            # Store initial field name before altering it for the lookup in the repository class
            field_backup = field

            # Extract data that belongs to the column
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

            # Store in dictionary
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
    """
    This function will store all tables from the given .sql file in a dictionary.
    The keys will be the columns which in turn are also dictionaries containing.
        - Datatype
        - Limits
        - Whether or note the column accepts nulls

    It also includes the original name of the table.
    This variable is used to construct the MySQL queries in the repository classes.

    :param data: content of the current .sql file as 1 string
    :return: dictionary described above
    """
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
    """
    This function will extract the name of the currently checked database
    using a regular expression

    :param data: content of the current .sql file as 1 string
    :return: name of the database
    """
    try:
        database_name = re.findall(r'CREATE +DATABASE +IF +NOT +EXISTS +`\w+`', data)[0]
        database_name = re.findall(r'`\w+`', database_name)[0][1:-1]
    except Exception:
        # No match
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


def regex_pattern(limit):
    pattern = ""

    if limit == "\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}":
        pattern = "yyyy-mm-dd hh:mm:ss"
    elif limit == "\d{4}-\d{2}-\d{2}":
        pattern = "yyyy-mm-dd"
    elif limit == "\d{2}:\d{2}:\d{2}":
        pattern = "hh:mm:ss"
    elif limit == "\d{4}":
        pattern = "yyyy"

    return pattern


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
                lines.append("\t" * tabs + "try:")
                lines.append("\t" * (tabs + 1) + "if len(re.findall(r'%s', value)[0]) == len(value):" % limit)
                lines.append("\t" * (tabs + 2) + "self._%s = str(value)" % prop)
                lines.append("\t" * (tabs + 1) + "else:")
                lines.append("\t" * (tabs + 2) +
                             "self._valueErrors[\"%s\"] = "
                             "ValueError(\"input voor %s match het patroon niet (%s)\")"
                             % (prop, prop, regex_pattern(limit)))
                lines.append("\t" * tabs + "except Exception:")
                lines.append("\t" * (tabs + 1) +
                             "self._valueErrors[\"%s\"] = "
                             "ValueError(\"input voor %s match het patroon niet (%s)\")"
                             % (prop, prop, regex_pattern(limit)))
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
    """
    This function will translate the datatype from MySQL terms to Python terms.
    It will also set limits when this is necessary
        - smallints vs mediumints
        - regular expressions for datetime, date, time, timestamp, year

    :param tabs: Amount of tabs used to outline the added lines
    :param lines: List of lines to append to (only comments)
    :param limits: Limits of the current column
    :param datatype: Datatype of the current column, in MySQL terms
    :return:
        - exact: whether the input value has to match the limits exactly, or just have to be <=
        - lines: updates list of lines, including the added comments
        - limits: limitations of the input value
        - datatype: datatype of the current column, in Python terms
    """
    exact = False

    if datatype == "varchar" or datatype == "longtext":
        datatype = "str"

    if datatype == "tinytext":
        datatype = "str"
        limits = ["255"]

    if datatype == "text":
        datatype = "str"
        limits = ["65535"]

    if datatype == "mediumtext":
        datatype = "str"
        limits = ["16777215"]

    if datatype == "longtext":
        datatype = "str"
        limits = ["4294967295"]

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


def validate_datatype(lines, datatype, prop, tabs, limits=None):
    """
    This function will generate the code that is used to validate the input value
    Firstly, the datatype is converted to Python terms, and the limits are updated accordingly

    :param lines:
    :param datatype:
    :param prop:
    :param tabs:
    :param limits:
    :return:
    """
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
    """
    This function will generate basic repository classes for each table.
    This repository class will yield all MySQL queries, as well as some utility functions,
    which are also generated for each table.
        - map to object of the correct class, with the correct parameters
        - check column

    :param repos: folder to store the repository classes
    :param database_name: name of the current database
    :param tables: dictionary of all tables that are in the current database
    """
    for table in tables.keys():
        # Initialize file
        lines = [
            # import the generated class that matches this table,
            # as well as the database connector class
            "from models.%s import %s" % (table, table),
            "from repositories.Database import Database",
            "",
            "",
            # Simple MySQL query to get all contents of the current table
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
            # Simple MySQL to get all contents of the current table, matching a certain condition on the primary key
            # Note the disabling of SQL injection
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
            # method to verify return value of the database
            "\t@staticmethod",
            "\tdef check_column(row, column_name):",
            "\t\tresult = None",
            "\t\tif column_name in row.keys() and row[column_name] is not None:",
            "\t\t\tresult = row[column_name]",
            "",
            "\t\treturn result",
            "",
            # Utility class to convert database result to an object of the generated class that matches this table
            "\t@staticmethod",
            "\tdef map_to_object(row):",
            "\t\tif row is not None and type(row) is dict:"
            # the next bit is dynamically generated in a loop
        ]

        # Lists for both the actual column names, and the altered ones
        real_properties = [tables[table][p]["real_name"] for p in tables[table].keys() if p != "original_table_name"]
        rewritten_properties = [p for p in tables[table].keys() if p != "original_table_name"]

        for prop, rewritten_prop in zip(real_properties, rewritten_properties):
            # Translate MySQL datatype to Python
            _, _, _, datatype = translate_datatype(
                0, [], [], tables[table][rewritten_prop]["datatype"]
            )

            # Validate and assign the value comming from the database
            lines.append("\t\t\t%s = %sRepository.check_column(row, \"%s\")" % (
                rewritten_prop, table, prop
            ))

            if datatype != "str":
                # Cast to the correct datatype if possible
                lines.append("\t\t\t%s = %s(%s) if %s is not None else None" % (
                    rewritten_prop, datatype, rewritten_prop, rewritten_prop
                ))

        lines.append("")
        lines.append("\t\treturn %s(%s)" % (
            table, ", ".join(rewritten_properties)
        ))

        # Write repository class to disk
        with open(os.path.join(repos, "%sRepository" % table) + ".py", "w") as f:
            f.writelines(["%s\n" % line.replace("\t", " "*4) for line in lines])


def generate_classes(models, tables):
    """
    This function will generate a class for each table in the current database.
    Each column is represented by a property that uses a setter function to validate all input.

    :param models: directory to store these classes
    :param tables: dictionary of all tables in the current database,
    as well as their columns and data on those columns
    """
    for table in tables.keys():
        # Initialize the file
        lines = [
            "import re",
            "",
            "",
            "class %s:" % table
        ]

        # Store properties in a list and format them a bit
        properties = [
            prop.lower() for prop in tables[table].keys()
            if prop != "original_table_name"
        ]

        # __init__
        lines.append("\tdef __init__(self, %s):" % ", ".join(properties))
        lines.append("\t\tself._valueErrors = dict()")
        for prop in properties:
            lines.append("\t\tself.%s = %s" % (prop, prop))

        # valueErrors property
        lines.append("\n\t@property")
        lines.append("\tdef valueErrors(self):")
        lines.append("\t\treturn self._valueErrors")

        # isValid property
        lines.append("\n\t@property")
        lines.append("\tdef isValid(self):")
        lines.append("\t\treturn len(self._valueErrors) == 0")

        # Custom getter and setter functions per column of the current table
        for prop in properties:
            # Pull variables out of the dictionary
            limits = tables[table][prop]["limits"]
            not_null = tables[table][prop]["not_null"]
            datatype = tables[table][prop]["datatype"].lower()

            # Getter
            lines.append("\n\t@property")
            lines.append("\tdef %s(self):" % prop)
            lines.append("\t\treturn self._%s" % prop)

            # Setter
            lines.append("\t@%s.setter" % prop)
            lines.append("\tdef %s(self, value):" % prop)
            if not_null:
                # This property CAN NOT be None
                lines.append("\t\t# Property CAN NOT be None")
                lines = validate_datatype(lines, datatype, prop, tabs=2, limits=limits)
            else:
                # This property CAN be None
                lines.append("\t\t# Property CAN be None")
                lines.append("\t\tif value is None:")
                lines.append("\t\t\tself._%s = value" % prop)
                lines.append("\t\telse:")
                lines = validate_datatype(lines, datatype, prop, tabs=3, limits=limits)

        # toString method
        lines.append("\n\tdef __str__(self):")
        lines.append("\t\treturn \"%s: %s: %%s\" %% self.%s" % (table, properties[0], properties[0]))

        # When printed in a list, copy format of toString method
        lines.append("\n\tdef __repr__(self):")
        lines.append("\t\tself.__str__()")

        # Writing the file to disk
        with open(os.path.join(models, table) + ".py", "w") as f:
            f.writelines(["%s\n" % line.replace("\t", " "*4) for line in lines])


def prepare_for_export(filepath, database_name):
    """
    This function defines and creates the necessary folders that the generated classes will be written to.
    These folders are cleared first so no previous export data is remaining

    :param filepath: filepath of the .sql file.
    The root folder of the exported code is placed in the same directory.
    :param database_name: The name of the database we are going to generate classes for.
    This name is used to name the root folder.
    :return: The filepaths of the root, models and repositories directories
    """
    # Define directories to store generated files
    root_dir = os.path.join(os.path.dirname(filepath), "%s_python" % database_name)
    models_dir = os.path.join(root_dir, "models")
    repositories_dir = os.path.join(root_dir, "repositories")

    # Clear previous exports
    if os.path.exists(root_dir):
        try:
            shutil.rmtree(root_dir, True)
        except Exception:
            pass

    # Create directories to store generated files
    os.makedirs(root_dir)
    os.makedirs(models_dir)
    os.makedirs(repositories_dir)

    return root_dir, models_dir, repositories_dir


def convert_file(filepath):
    """
    This is the main directory of the project.
    Here, the content of the current .sql file is read and stored.

    This data will be used to extract
        - The name of the database
        - The tables of the database
        - The columns of these tables
        - The data of these columns (datatype, limits, allowing nulls)

    When all of the data is gathered, it will be used to generate classes.
    These classes are exact replicas of the table they represent.
    They will only allow data to go in that is absolutely valid, but manual checks are always recommended.

    Lastly, it will generate basic repository classes, including some basic SQL queries

    :param filepath: filepath of the current .sql file
    """

    # Read data
    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read().replace('\n', ' ').replace('\r', '')

    # Make the data more meaningful
    database_name = get_database_name(data)
    tables = get_database_tables(data)

    # Define and create export folders
    root_dir, models_dir, repositories_dir = prepare_for_export(filepath, database_name)

    # Generate files
    generate_classes(models_dir, tables)
    generate_repositories(repositories_dir, database_name, tables)


def main():
    """
    This function will list all .sql files in the sql folder.
    It will then call to convert all columns of all tables into Python classes.
    """
    sql_files = get_sql_files()
    for f in sql_files:
        try:
            convert_file(f)
            print("Succesfully converted %s" % os.path.splitext(os.path.basename(f))[0])
        except Exception as ex:
            print("Unable to read data from %s -- %s" % (f, ex))
            break


if __name__ == '__main__':
    import os
    import re
    import shutil

    main()
