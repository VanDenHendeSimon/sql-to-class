import re


class Verzenders:
	def __init__(self, verzendid, bedrijf, telefoonnummer):
		self._valueErrors = dict()
		self.verzendid = verzendid
		self.bedrijf = bedrijf
		self.telefoonnummer = telefoonnummer

	@property
	def valueErrors(self):
		return self._valueErrors

	@property
	def isValid(self):
		return len(self._valueErrors) == 0

	@property
	def verzendid(self):
		return self._verzendid
	@verzendid.setter
	def verzendid(self, value):
		# Property CAN NOT be None
		# smallint
		if type(value) is int:
			if -32768 < value < 32767:
				self._verzendid = value
			else:
				self._valueErrors["verzendid"] = ValueError("input voor verzendid is te groot / klein")
		else:
			self._valueErrors["verzendid"] = ValueError("input voor verzendid is ongeldig")

	@property
	def bedrijf(self):
		return self._bedrijf
	@bedrijf.setter
	def bedrijf(self, value):
		# Property CAN be None
		if value is None:
			self._bedrijf = value
		else:
			if type(value) is str:
				if len(str(value)) <= 255:
					self._bedrijf = str(value)
				else:
					self._valueErrors["bedrijf"] = ValueError("input voor bedrijf is te lang")
			else:
				self._valueErrors["bedrijf"] = ValueError("input voor bedrijf is ongeldig")

	@property
	def telefoonnummer(self):
		return self._telefoonnummer
	@telefoonnummer.setter
	def telefoonnummer(self, value):
		# Property CAN be None
		if value is None:
			self._telefoonnummer = value
		else:
			if type(value) is str:
				if len(str(value)) <= 12:
					self._telefoonnummer = str(value)
				else:
					self._valueErrors["telefoonnummer"] = ValueError("input voor telefoonnummer is te lang")
			else:
				self._valueErrors["telefoonnummer"] = ValueError("input voor telefoonnummer is ongeldig")

	def __str__(self):
		return "Verzenders: verzendid: %s" % self.verzendid

	def __repr__(self):
		self.__str__()
