from models.Vluchtinformatie import Vluchtinformatie
from repositories.Database import Database


class VluchtinformatieRepository:
	@ staticmethod
	def read_all():
		result = []
		sql = "SELECT * FROM vliegtuigen.tblvluchtinformatie"
		rows = Database.get_rows(sql)

		if rows is not None:
			for row in rows:
				# mapping naar object
				result.append(VluchtinformatieRepository.map_to_object(row))

		return result

	@staticmethod
	def read_single(_id):
		if not _id:
			return "Ongedlig ID. Probeer opnieuw"

		sql = """
		SELECT
			*
		FROM vliegtuigen.tblvluchtinformatie
		WHERE vluchtnr = %s
		"""
		params = [_id]

		result = Database.get_one_row(sql, params)

		if type(result) is dict:
			# Mapping naar Vluchtinformatie object
			 result = VluchtinformatieRepository.map_to_object(result)

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
			vluchtnr = VluchtinformatieRepository.check_column(row, "VluchtNr")
			vluchtnr = int(vluchtnr) if vluchtnr is not None else None

			stoelnr = VluchtinformatieRepository.check_column(row, "StoelNr")
			stoelnr = int(stoelnr) if stoelnr is not None else None

			klantid = VluchtinformatieRepository.check_column(row, "KlantID")
			klantid = int(klantid) if klantid is not None else None

			prijsbetaaldvoorstoel = VluchtinformatieRepository.check_column(row, "PrijsBetaaldVoorStoel")
			prijsbetaaldvoorstoel = float(prijsbetaaldvoorstoel) if prijsbetaaldvoorstoel is not None else None


		return Vluchtinformatie(vluchtnr, stoelnr, klantid, prijsbetaaldvoorstoel)
