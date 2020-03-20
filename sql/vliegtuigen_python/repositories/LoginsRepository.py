from models.Logins import Logins
from repositories.Database import Database


class LoginsRepository:
	@ staticmethod
	def read_all():
		result = []
		sql = "SELECT * FROM vliegtuigen.tbllogins"
		rows = Database.get_rows(sql)

		if rows is not None:
			for row in rows:
				# mapping naar object
				result.append(LoginsRepository.map_to_object(row))

		return result

	@staticmethod
	def read_single(_id):
		if not _id:
			return "Ongedlig ID. Probeer opnieuw"

		sql = """
		SELECT
			*
		FROM vliegtuigen.tbllogins
		WHERE loginid = %s
		"""
		params = [_id]

		result = Database.get_one_row(sql, params)

		if type(result) is dict:
			# Mapping naar Logins object
			 result = LoginsRepository.map_to_object(result)

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
			loginid = LoginsRepository.check_column(row, "loginID")
			loginid = int(loginid) if loginid is not None else None

			voornaam = LoginsRepository.check_column(row, "voornaam")
			naam = LoginsRepository.check_column(row, "naam")
			paswoord = LoginsRepository.check_column(row, "paswoord")
			gebdatum = LoginsRepository.check_column(row, "gebdatum")
			login = LoginsRepository.check_column(row, "login")

		return Logins(loginid, voornaam, naam, paswoord, gebdatum, login)
