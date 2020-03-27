from models.Verzenders import Verzenders
from repositories.Database import Database


class VerzendersRepository:
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
        sql = "SELECT * FROM artemis.tblverzenders"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(VerzendersRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM artemis.tblverzenders
        WHERE verzendid = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Verzenders object
             result = VerzendersRepository.map_to_object(result)

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
            verzendid = VerzendersRepository.check_column(row, "VerzendID")
            verzendid = int(verzendid) if verzendid is not None else None
            bedrijf = VerzendersRepository.check_column(row, "Bedrijf")
            telefoonnummer = VerzendersRepository.check_column(row, "Telefoonnummer")

        return Verzenders(verzendid, bedrijf, telefoonnummer)
