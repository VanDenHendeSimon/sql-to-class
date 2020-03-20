from models.Leveranciers import Leveranciers
from repositories.Database import Database


class LeveranciersRepository:
	@ staticmethod
	def read_all():
		result = []
		sql = "SELECT * FROM artemis.tblleveranciers"
		rows = Database.get_rows(sql)

		if rows is not None:
			for row in rows:
				# mapping naar object
				result.append(LeveranciersRepository.map_to_object(row))

		return result

	@staticmethod
	def read_single(_id):
		if not _id:
			return "Ongedlig ID. Probeer opnieuw"

		sql = """
		SELECT
			*
		FROM artemis.tblleveranciers
		WHERE leveranciersnummer = %s
		"""
		params = [_id]

		result = Database.get_one_row(sql, params)

		if type(result) is dict:
			# Mapping naar Leveranciers object
			 result = LeveranciersRepository.map_to_object(result)

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
			leveranciersnummer = LeveranciersRepository.check_column(row, "Leveranciersnummer")
			leveranciersnummer = int(leveranciersnummer) if leveranciersnummer is not None else None

			bedrijf = LeveranciersRepository.check_column(row, "Bedrijf")
			adres = LeveranciersRepository.check_column(row, "Adres")
			plaats = LeveranciersRepository.check_column(row, "Plaats")
			postcode = LeveranciersRepository.check_column(row, "Postcode")
			land = LeveranciersRepository.check_column(row, "Land")
			url = LeveranciersRepository.check_column(row, "URL")

		return Leveranciers(leveranciersnummer, bedrijf, adres, plaats, postcode, land, url)
