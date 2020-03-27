from models.Klanten import Klanten
from repositories.Database import Database


class KlantenRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            data = request.get_json()
        else:
            data = request.form.to_dict()

        return data

    @staticmethod
    def read_all():
        result = []
        sql = "SELECT * FROM artemis.tblklanten"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(KlantenRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM artemis.tblklanten
        WHERE klantnummer = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Klanten object
             result = KlantenRepository.map_to_object(result)

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
            klantnummer = KlantenRepository.check_column(row, "Klantnummer")
            klantnummer = int(klantnummer) if klantnummer is not None else None
            naam = KlantenRepository.check_column(row, "Naam")
            straat = KlantenRepository.check_column(row, "Straat")
            postnr = KlantenRepository.check_column(row, "Postnr")
            gemeente = KlantenRepository.check_column(row, "Gemeente")
            ondernemingsnr = KlantenRepository.check_column(row, "Ondernemingsnr")
            type_klanten = KlantenRepository.check_column(row, "Type")
            saldo = KlantenRepository.check_column(row, "Saldo")
            saldo = float(saldo) if saldo is not None else None
            opmerking = KlantenRepository.check_column(row, "Opmerking")

        return Klanten(klantnummer, naam, straat, postnr, gemeente, ondernemingsnr, type_klanten, saldo, opmerking)
