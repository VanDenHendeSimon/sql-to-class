from models.Treinen import Treinen
from repositories.Database import Database


class TreinenRepository:
    @staticmethod
    def json_or_formdata(request):
        """This function is only necessary when using the repo in the backend of an api"""
        if request.content_type == 'application/json':
            data = request.get_json()
        else:
            data = request.form.to_dict()

        return data

    @staticmethod
    def read_all():
        result = []
        sql = "SELECT * FROM trein.treinen"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(TreinenRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM trein.treinen
        WHERE idtrein = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Treinen object
             result = TreinenRepository.map_to_object(result)

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
            idtrein = TreinenRepository.check_column(row, "idtrein")
            idtrein = int(idtrein) if idtrein is not None else None
            vertrek = TreinenRepository.check_column(row, "vertrek")
            bestemmingid = TreinenRepository.check_column(row, "bestemmingID")
            bestemmingid = int(bestemmingid) if bestemmingid is not None else None
            spoor = TreinenRepository.check_column(row, "spoor")
            spoor = int(spoor) if spoor is not None else None
            vertraging = TreinenRepository.check_column(row, "vertraging")
            vertraging = int(vertraging) if vertraging is not None else None
            afgeschaft = TreinenRepository.check_column(row, "afgeschaft")
            afgeschaft = int(afgeschaft) if afgeschaft is not None else None

        return Treinen(idtrein, vertrek, bestemmingid, spoor, vertraging, afgeschaft)
