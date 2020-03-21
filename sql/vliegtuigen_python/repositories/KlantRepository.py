from models.Klant import Klant
from repositories.Database import Database


class KlantRepository:
    @ staticmethod
    def read_all():
        result = []
        sql = "SELECT * FROM vliegtuigen.tblklant"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(KlantRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM vliegtuigen.tblklant
        WHERE klantid = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Klant object
             result = KlantRepository.map_to_object(result)

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
            klantid = KlantRepository.check_column(row, "KlantID")
            klantid = int(klantid) if klantid is not None else None
            fnaam = KlantRepository.check_column(row, "FNaam")
            vnaam = KlantRepository.check_column(row, "VNaam")
            straat = KlantRepository.check_column(row, "Straat")
            nummer = KlantRepository.check_column(row, "Nummer")
            postcode = KlantRepository.check_column(row, "Postcode")
            postcode = int(postcode) if postcode is not None else None
            gemeente = KlantRepository.check_column(row, "Gemeente")

        return Klant(klantid, fnaam, vnaam, straat, nummer, postcode, gemeente)
