from models.Btwtarief import Btwtarief
from repositories.Database import Database


class BtwtariefRepository:
    @ staticmethod
    def read_all():
        result = []
        sql = "SELECT * FROM artemis.tblbtwtarief"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(BtwtariefRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM artemis.tblbtwtarief
        WHERE btwcode = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Btwtarief object
             result = BtwtariefRepository.map_to_object(result)

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
            btwcode = BtwtariefRepository.check_column(row, "BTWCode")
            btwcode = int(btwcode) if btwcode is not None else None
            btwpercentage = BtwtariefRepository.check_column(row, "BTWPercentage")
            btwpercentage = float(btwpercentage) if btwpercentage is not None else None

        return Btwtarief(btwcode, btwpercentage)
