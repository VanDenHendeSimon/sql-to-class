from models.Bestemming import Bestemming
from repositories.Database import Database


class BestemmingRepository:
    @ staticmethod
    def read_all():
        result = []
        sql = "SELECT * FROM vliegtuigen.tblbestemming"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(BestemmingRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM vliegtuigen.tblbestemming
        WHERE bestemmingid = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Bestemming object
             result = BestemmingRepository.map_to_object(result)

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
            bestemmingid = BestemmingRepository.check_column(row, "BestemmingID")
            bestemmingid = int(bestemmingid) if bestemmingid is not None else None

            afkorting = BestemmingRepository.check_column(row, "Afkorting")
            voluit = BestemmingRepository.check_column(row, "Voluit")
            land = BestemmingRepository.check_column(row, "Land")
            typevlucht = BestemmingRepository.check_column(row, "TypeVlucht")
            typevlucht = int(typevlucht) if typevlucht is not None else None


        return Bestemming(bestemmingid, afkorting, voluit, land, typevlucht)
