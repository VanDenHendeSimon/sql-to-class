from models.Orders import Orders
from repositories.Database import Database


class OrdersRepository:
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
        sql = "SELECT * FROM artemis.tblorders"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(OrdersRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM artemis.tblorders
        WHERE orderid = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Orders object
             result = OrdersRepository.map_to_object(result)

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
            orderid = OrdersRepository.check_column(row, "OrderID")
            orderid = int(orderid) if orderid is not None else None
            klantnummer = OrdersRepository.check_column(row, "Klantnummer")
            klantnummer = int(klantnummer) if klantnummer is not None else None
            werknemerid = OrdersRepository.check_column(row, "WerknemerID")
            werknemerid = int(werknemerid) if werknemerid is not None else None
            verzendid = OrdersRepository.check_column(row, "VerzendID")
            verzendid = int(verzendid) if verzendid is not None else None
            orderdatum = OrdersRepository.check_column(row, "Orderdatum")
            vervaldatum = OrdersRepository.check_column(row, "Vervaldatum")
            leverdatum = OrdersRepository.check_column(row, "Leverdatum")
            vrachtkosten = OrdersRepository.check_column(row, "Vrachtkosten")
            vrachtkosten = float(vrachtkosten) if vrachtkosten is not None else None

        return Orders(orderid, klantnummer, werknemerid, verzendid, orderdatum, vervaldatum, leverdatum, vrachtkosten)
