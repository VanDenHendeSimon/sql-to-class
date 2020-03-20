from models.Categorieen import Categorieen
from repositories.Database import Database


class CategorieenRepository:
	@ staticmethod
	def read_all():
		result = []
		sql = "SELECT * FROM artemis.tblcategorieen"
		rows = Database.get_rows(sql)

		if rows is not None:
			for row in rows:
				# mapping naar object
				result.append(CategorieenRepository.map_to_object(row))

		return result

	@staticmethod
	def read_single(_id):
		if not _id:
			return "Ongedlig ID. Probeer opnieuw"

		sql = """
		SELECT
			*
		FROM artemis.tblcategorieen
		WHERE categorienummer = %s
		"""
		params = [_id]

		result = Database.get_one_row(sql, params)

		if type(result) is dict:
			# Mapping naar Categorieen object
			 result = CategorieenRepository.map_to_object(result)

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
			categorienummer = CategorieenRepository.check_column(row, "Categorienummer")
			categorienummer = int(categorienummer) if categorienummer is not None else None

			categorienaam = CategorieenRepository.check_column(row, "Categorienaam")
			bijschrijving = CategorieenRepository.check_column(row, "Bijschrijving")

		return Categorieen(categorienummer, categorienaam, bijschrijving)
