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

	@property
	def bedrijf(self):
		return self._bedrijf
	@bedrijf.setter
	def bedrijf(self, value):
		if value is None:
			self._bedrijf = value
		else:
			if len(str(value)) <= 255:
				self._bedrijf = str(value)
			else:
				self._valueErrors["bedrijf"] = ValueError("input voor bedrijf is te lang")

	@property
	def telefoonnummer(self):
		return self._telefoonnummer
	@telefoonnummer.setter
	def telefoonnummer(self, value):
		if value is None:
			self._telefoonnummer = value
		else:
			if len(str(value)) <= 12:
				self._telefoonnummer = str(value)
			else:
				self._valueErrors["telefoonnummer"] = ValueError("input voor telefoonnummer is te lang")

	def __str__(self):
		return "Verzenders: verzendid: %s" % self.verzendid

	def __repr__(self):
		self.__str__()
