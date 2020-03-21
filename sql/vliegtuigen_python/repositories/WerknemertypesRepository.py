from models.Werknemertypes import Werknemertypes
from repositories.Database import Database


class WerknemertypesRepository:
    @ staticmethod
    def read_all():
        result = []
        sql = "SELECT * FROM vliegtuigen.tblwerknemertypes"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(WerknemertypesRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM vliegtuigen.tblwerknemertypes
        WHERE typeid = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Werknemertypes object
             result = WerknemertypesRepository.map_to_object(result)

        return result

    @staticmethod
    def check_column(row, column_name):
        result = None
        if column_name in row.keys() and row[column_name] is not None:
            result = row[column_name]

        return result

    @staticmethod
    def map_to_object(row):
        if row is not None and type(row) is dict:
            typeid = WerknemertypesRepository.check_column(row, "TypeID")
            typeid = int(typeid) if typeid is not None else None

            omschrijving = WerknemertypesRepository.check_column(row, "Omschrijving")

        return Werknemertypes(typeid, omschrijving)
