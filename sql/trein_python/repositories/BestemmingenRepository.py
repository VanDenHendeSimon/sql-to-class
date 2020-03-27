from models.Bestemmingen import Bestemmingen
from repositories.Database import Database


class BestemmingenRepository:
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
        sql = "SELECT * FROM trein.bestemmingen"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(BestemmingenRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM trein.bestemmingen
        WHERE idbestemming = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Bestemmingen object
             result = BestemmingenRepository.map_to_object(result)

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
            idbestemming = BestemmingenRepository.check_column(row, "idbestemming")
            idbestemming = int(idbestemming) if idbestemming is not None else None
            stad = BestemmingenRepository.check_column(row, "stad")
            latitude = BestemmingenRepository.check_column(row, "latitude")
            llngitude = BestemmingenRepository.check_column(row, "Llngitude")

        return Bestemmingen(idbestemming, stad, latitude, llngitude)
