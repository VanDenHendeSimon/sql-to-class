from models.Vliegtuig import Vliegtuig
from repositories.Database import Database


class VliegtuigRepository:
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
        sql = "SELECT * FROM vliegtuigen.tblvliegtuig"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(VliegtuigRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM vliegtuigen.tblvliegtuig
        WHERE vliegtuigid = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Vliegtuig object
             result = VliegtuigRepository.map_to_object(result)

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
            vliegtuigid = VliegtuigRepository.check_column(row, "VliegtuigID")
            vliegtuigid = int(vliegtuigid) if vliegtuigid is not None else None
            vliegtuigbouwer = VliegtuigRepository.check_column(row, "Vliegtuigbouwer")
            type_vliegtuig = VliegtuigRepository.check_column(row, "Type")
            maxaantalzitplaatsenindittoestel = VliegtuigRepository.check_column(row, "MaxAantalZitplaatsenInDitToestel")
            maxaantalzitplaatsenindittoestel = int(maxaantalzitplaatsenindittoestel) if maxaantalzitplaatsenindittoestel is not None else None
            internecode = VliegtuigRepository.check_column(row, "InterneCode")

        return Vliegtuig(vliegtuigid, vliegtuigbouwer, type_vliegtuig, maxaantalzitplaatsenindittoestel, internecode)
