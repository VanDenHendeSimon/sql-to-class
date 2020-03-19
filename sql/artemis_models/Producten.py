class Producten:
	def __init__(self, productnummer, leveranciersnummer, categorienummer, productnaam, nederlandsenaam, hoeveelheidpereenheid, prijspereenheid, voorraad, btwcode, inbestelling, bestelpunt, uitassortiment):
		self._valueErrors = dict()
		self.productnummer = productnummer
		self.leveranciersnummer = leveranciersnummer
		self.categorienummer = categorienummer
		self.productnaam = productnaam
		self.nederlandsenaam = nederlandsenaam
		self.hoeveelheidpereenheid = hoeveelheidpereenheid
		self.prijspereenheid = prijspereenheid
		self.voorraad = voorraad
		self.btwcode = btwcode
		self.inbestelling = inbestelling
		self.bestelpunt = bestelpunt
		self.uitassortiment = uitassortiment

	@property
	def valueErrors(self):
		return self._valueErrors

	@property
	def isValid(self):
		return len(self._valueErrors) == 0

	@property
	def productnummer(self):
		return self._productnummer
	@productnummer.setter
	def productnummer(self, value):
		if type(value) is int:
			self._productnummer = value
		else:
			self._valueErrors["productnummer"] = ValueError("input voor productnummer is ongeldig")

	@property
	def leveranciersnummer(self):
		return self._leveranciersnummer
	@leveranciersnummer.setter
	def leveranciersnummer(self, value):
		if value is None:
			self._leveranciersnummer = value
		else:
			self._leveranciersnummer = str(value)

	@property
	def categorienummer(self):
		return self._categorienummer
	@categorienummer.setter
	def categorienummer(self, value):
		if value is None:
			self._categorienummer = value
		else:
			self._categorienummer = str(value)

	@property
	def productnaam(self):
		return self._productnaam
	@productnaam.setter
	def productnaam(self, value):
		if type(value) is str:
			if len(value) <= 40:
				self._productnaam = value
			else:
				self._valueErrors["productnaam"] = ValueError("input voor productnaam is te lang")
		else:
			self._valueErrors["productnaam"] = ValueError("input voor productnaam is ongeldig")

	@property
	def nederlandsenaam(self):
		return self._nederlandsenaam
	@nederlandsenaam.setter
	def nederlandsenaam(self, value):
		if value is None:
			self._nederlandsenaam = value
		else:
			if len(str(value)) <= 50:
				self._nederlandsenaam = str(value)
			else:
				self._valueErrors["nederlandsenaam"] = ValueError("input voor nederlandsenaam is te lang")

	@property
	def hoeveelheidpereenheid(self):
		return self._hoeveelheidpereenheid
	@hoeveelheidpereenheid.setter
	def hoeveelheidpereenheid(self, value):
		if value is None:
			self._hoeveelheidpereenheid = value
		else:
			if len(str(value)) <= 20:
				self._hoeveelheidpereenheid = str(value)
			else:
				self._valueErrors["hoeveelheidpereenheid"] = ValueError("input voor hoeveelheidpereenheid is te lang")

	@property
	def prijspereenheid(self):
		return self._prijspereenheid
	@prijspereenheid.setter
	def prijspereenheid(self, value):
		if value is None:
			self._prijspereenheid = value
		else:
			if "." in str(value):
				if ((len(str(value).split(".")[0]) <= 15) and (len(str(value).split(".")[1]) <= 4)):
					self._prijspereenheid = value
				else:
					self._valueErrors["prijspereenheid"] = ValueError("input voor prijspereenheid is te lang")
			else:
				if len(str(value)) <= 19:
					self._prijspereenheid = value
				else:
					self._valueErrors["prijspereenheid"] = ValueError("input voor prijspereenheid is te lang")

	@property
	def voorraad(self):
		return self._voorraad
	@voorraad.setter
	def voorraad(self, value):
		if value is None:
			self._voorraad = value
		else:
			self._voorraad = str(value)

	@property
	def btwcode(self):
		return self._btwcode
	@btwcode.setter
	def btwcode(self, value):
		if value is None:
			self._btwcode = value
		else:
			self._btwcode = str(value)

	@property
	def inbestelling(self):
		return self._inbestelling
	@inbestelling.setter
	def inbestelling(self, value):
		if value is None:
			self._inbestelling = value
		else:
			self._inbestelling = str(value)

	@property
	def bestelpunt(self):
		return self._bestelpunt
	@bestelpunt.setter
	def bestelpunt(self, value):
		if value is None:
			self._bestelpunt = value
		else:
			self._bestelpunt = str(value)

	@property
	def uitassortiment(self):
		return self._uitassortiment
	@uitassortiment.setter
	def uitassortiment(self, value):

	def __str__(self):
		return "Producten: productnummer: %s" % self.productnummer

	def __repr__(self):
		self.__str__()
