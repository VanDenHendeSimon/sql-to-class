from models.Orderinformatie import Orderinformatie
from repositories.Database import Database


class OrderinformatieRepository:
	@ staticmethod
	def read_all():
		result = []
		sql = "SELECT * FROM artemis.tblorderinformatie"
		rows = Database.get_rows(sql)

		if rows is not None:
			for row in rows:
				# mapping naar object
				result.append(OrderinformatieRepository.map_to_object(row))

		return result

	@staticmethod
	def read_single(_id):
		if not _id:
			return "Ongedlig ID. Probeer opnieuw"

		sql = """
		SELECT
			*
		FROM artemis.tblorderinformatie
		WHERE orderid = %s
		"""
		params = [_id]

		result = Database.get_one_row(sql, params)

		if type(result) is dict:
			# Mapping naar Orderinformatie object
			 result = OrderinformatieRepository.map_to_object(result)

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
			orderid = OrderinformatieRepository.check_column(row, "OrderID")
			orderid = int(orderid) if orderid is not None else None

			productnummer = OrderinformatieRepository.check_column(row, "Productnummer")
			productnummer = int(productnummer) if productnummer is not None else None

			hoeveelheid = OrderinformatieRepository.check_column(row, "Hoeveelheid")
			hoeveelheid = float(hoeveelheid) if hoeveelheid is not None else None

			korting = OrderinformatieRepository.check_column(row, "Korting")
			korting = float(korting) if korting is not None else None


		return Orderinformatie(orderid, productnummer, hoeveelheid, korting)
