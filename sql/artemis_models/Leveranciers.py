class Leveranciers:
	def __init__(self, leveranciersnummer, bedrijf, adres, plaats, postcode, land, url):
		self._valueErrors = dict()
		self.leveranciersnummer = leveranciersnummer
		self.bedrijf = bedrijf
		self.adres = adres
		self.plaats = plaats
		self.postcode = postcode
		self.land = land
		self.url = url

	@property
	def valueErrors(self):
		return self._valueErrors

	@property
	def isValid(self):
		return len(self._valueErrors) == 0

	@property
	def leveranciersnummer(self):
		return self._leveranciersnummer
	@leveranciersnummer.setter
	def leveranciersnummer(self, value):
		if type(value) is int:
			self._leveranciersnummer = value
		else:
			self._valueErrors["leveranciersnummer"] = ValueError("input voor leveranciersnummer is ongeldig")

	@property
	def bedrijf(self):
		return self._bedrijf
	@bedrijf.setter
	def bedrijf(self, value):
		if value is None:
			self._bedrijf = value
		else:
			if len(str(value)) <= 50:
				self._bedrijf = str(value)
			else:
				self._valueErrors["bedrijf"] = ValueError("input voor bedrijf is te lang")

	@property
	def adres(self):
		return self._adres
	@adres.setter
	def adres(self, value):
		if value is None:
			self._adres = value
		else:
			if len(str(value)) <= 50:
				self._adres = str(value)
			else:
				self._valueErrors["adres"] = ValueError("input voor adres is te lang")

	@property
	def plaats(self):
		return self._plaats
	@plaats.setter
	def plaats(self, value):
		if value is None:
			self._plaats = value
		else:
			if len(str(value)) <= 50:
				self._plaats = str(value)
			else:
				self._valueErrors["plaats"] = ValueError("input voor plaats is te lang")

	@property
	def postcode(self):
		return self._postcode
	@postcode.setter
	def postcode(self, value):
		if value is None:
			self._postcode = value
		else:
			if len(str(value)) <= 50:
				self._postcode = str(value)
			else:
				self._valueErrors["postcode"] = ValueError("input voor postcode is te lang")

	@property
	def land(self):
		return self._land
	@land.setter
	def land(self, value):
		if value is None:
			self._land = value
		else:
			if len(str(value)) <= 50:
				self._land = str(value)
			else:
				self._valueErrors["land"] = ValueError("input voor land is te lang")

	@property
	def url(self):
		return self._url
	@url.setter
	def url(self, value):
		if value is None:
			self._url = value
		else:
			self._url = str(value)

	def __str__(self):
		return "Leveranciers: leveranciersnummer: %s" % self.leveranciersnummer

	def __repr__(self):
		self.__str__()
