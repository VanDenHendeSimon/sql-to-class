from models.Huidigeprijssetting import Huidigeprijssetting
from repositories.Database import Database


class HuidigeprijssettingRepository:
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
        sql = "SELECT * FROM vliegtuigen.tblhuidigeprijssetting"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(HuidigeprijssettingRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM vliegtuigen.tblhuidigeprijssetting
        WHERE typevlucht = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Huidigeprijssetting object
             result = HuidigeprijssettingRepository.map_to_object(result)

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
            typevlucht = HuidigeprijssettingRepository.check_column(row, "TypeVlucht")
            typevlucht = int(typevlucht) if typevlucht is not None else None
            huidigeprijssetting = HuidigeprijssettingRepository.check_column(row, "HuidigePrijsSetting")
            huidigeprijssetting = float(huidigeprijssetting) if huidigeprijssetting is not None else None
            omschrijving = HuidigeprijssettingRepository.check_column(row, "omschrijving")

        return Huidigeprijssetting(typevlucht, huidigeprijssetting, omschrijving)
