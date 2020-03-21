from models.Vlucht import Vlucht
from repositories.Database import Database


class VluchtRepository:
    @ staticmethod
    def read_all():
        result = []
        sql = "SELECT * FROM vliegtuigen.tblvlucht"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(VluchtRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM vliegtuigen.tblvlucht
        WHERE vluchtnr = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Vlucht object
             result = VluchtRepository.map_to_object(result)

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
            vluchtnr = VluchtRepository.check_column(row, "VluchtNr")
            vluchtnr = int(vluchtnr) if vluchtnr is not None else None

            vluchtdatum = VluchtRepository.check_column(row, "Vluchtdatum")
            bestemmingid = VluchtRepository.check_column(row, "BestemmingID")
            bestemmingid = int(bestemmingid) if bestemmingid is not None else None

            vliegtuigid = VluchtRepository.check_column(row, "VliegtuigID")
            vliegtuigid = int(vliegtuigid) if vliegtuigid is not None else None


        return Vlucht(vluchtnr, vluchtdatum, bestemmingid, vliegtuigid)
