from models.Werknemer import Werknemer
from repositories.Database import Database


class WerknemerRepository:
	@ staticmethod
	def read_all():
		result = []
		sql = "SELECT * FROM vliegtuigen.tblwerknemer"
		rows = Database.get_rows(sql)

		if rows is not None:
			for row in rows:
				# mapping naar object
				result.append(WerknemerRepository.map_to_object(row))

		return result

	@staticmethod
	def read_single(_id):
		if not _id:
			return "Ongedlig ID. Probeer opnieuw"

		sql = """
		SELECT
			*
		FROM vliegtuigen.tblwerknemer
		WHERE werknemerid = %s
		"""
		params = [_id]

		result = Database.get_one_row(sql, params)

		if type(result) is dict:
			# Mapping naar Werknemer object
			 result = WerknemerRepository.map_to_object(result)

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
			werknemerid = WerknemerRepository.check_column(row, "WerknemerID")
			werknemerid = int(werknemerid) if werknemerid is not None else None

			naam = WerknemerRepository.check_column(row, "Naam")
			typeid = WerknemerRepository.check_column(row, "TypeID")
			typeid = int(typeid) if typeid is not None else None

			foto = WerknemerRepository.check_column(row, "Foto")

		return Werknemer(werknemerid, naam, typeid, foto)
