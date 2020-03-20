import re


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
		# Property CAN NOT be None
		# regular int
		if type(value) is int:
			if -2147483648 < value < 2147483647:
				self._productnummer = value
			else:
				self._valueErrors["productnummer"] = ValueError("input voor productnummer is te groot / klein")
		else:
			self._valueErrors["productnummer"] = ValueError("input voor productnummer is ongeldig")

	@property
	def leveranciersnummer(self):
		return self._leveranciersnummer
	@leveranciersnummer.setter
	def leveranciersnummer(self, value):
		# Property CAN be None
		if value is None:
			self._leveranciersnummer = value
		else:
			# regular int
			if type(value) is int:
				if -2147483648 < value < 2147483647:
					self._leveranciersnummer = value
				else:
					self._valueErrors["leveranciersnummer"] = ValueError("input voor leveranciersnummer is te groot / klein")
			else:
				self._valueErrors["leveranciersnummer"] = ValueError("input voor leveranciersnummer is ongeldig")

	@property
	def categorienummer(self):
		return self._categorienummer
	@categorienummer.setter
	def categorienummer(self, value):
		# Property CAN be None
		if value is None:
			self._categorienummer = value
		else:
			# regular int
			if type(value) is int:
				if -2147483648 < value < 2147483647:
					self._categorienummer = value
				else:
					self._valueErrors["categorienummer"] = ValueError("input voor categorienummer is te groot / klein")
			else:
				self._valueErrors["categorienummer"] = ValueError("input voor categorienummer is ongeldig")

	@property
	def productnaam(self):
		return self._productnaam
	@productnaam.setter
	def productnaam(self, value):
		# Property CAN NOT be None
		if type(value) is str:
			if len(str(value)) <= 40:
				self._productnaam = str(value)
			else:
				self._valueErrors["productnaam"] = ValueError("input voor productnaam is te lang")
		else:
			self._valueErrors["productnaam"] = ValueError("input voor productnaam is ongeldig")

	@property
	def nederlandsenaam(self):
		return self._nederlandsenaam
	@nederlandsenaam.setter
	def nederlandsenaam(self, value):
		# Property CAN be None
		if value is None:
			self._nederlandsenaam = value
		else:
			if type(value) is str:
				if len(str(value)) <= 50:
					self._nederlandsenaam = str(value)
				else:
					self._valueErrors["nederlandsenaam"] = ValueError("input voor nederlandsenaam is te lang")
			else:
				self._valueErrors["nederlandsenaam"] = ValueError("input voor nederlandsenaam is ongeldig")

	@property
	def hoeveelheidpereenheid(self):
		return self._hoeveelheidpereenheid
	@hoeveelheidpereenheid.setter
	def hoeveelheidpereenheid(self, value):
		# Property CAN be None
		if value is None:
			self._hoeveelheidpereenheid = value
		else:
			if type(value) is str:
				if len(str(value)) <= 20:
					self._hoeveelheidpereenheid = str(value)
				else:
					self._valueErrors["hoeveelheidpereenheid"] = ValueError("input voor hoeveelheidpereenheid is te lang")
			else:
				self._valueErrors["hoeveelheidpereenheid"] = ValueError("input voor hoeveelheidpereenheid is ongeldig")

	@property
	def prijspereenheid(self):
		return self._prijspereenheid
	@prijspereenheid.setter
	def prijspereenheid(self, value):
		# Property CAN be None
		if value is None:
			self._prijspereenheid = value
		else:
			if type(value) is float:
				if "." in str(value):
					if ((len(str(value).split(".")[0]) <= 15) and (len(str(value).split(".")[1]) <= 4)):
						self._prijspereenheid = value
					else:
						self._valueErrors["prijspereenheid"] = ValueError("input voor prijspereenheid is te groot / klein")
				else:
					if len(str(value)) <= 19:
						self._prijspereenheid = value
					else:
						self._valueErrors["prijspereenheid"] = ValueError("input voor prijspereenheid is te lang")
			else:
				self._valueErrors["prijspereenheid"] = ValueError("input voor prijspereenheid is ongeldig")

	@property
	def voorraad(self):
		return self._voorraad
	@voorraad.setter
	def voorraad(self, value):
		# Property CAN be None
		if value is None:
			self._voorraad = value
		else:
			# smallint
			if type(value) is int:
				if -32768 < value < 32767:
					self._voorraad = value
				else:
					self._valueErrors["voorraad"] = ValueError("input voor voorraad is te groot / klein")
			else:
				self._valueErrors["voorraad"] = ValueError("input voor voorraad is ongeldig")

	@property
	def btwcode(self):
		return self._btwcode
	@btwcode.setter
	def btwcode(self, value):
		# Property CAN be None
		if value is None:
			self._btwcode = value
		else:
			# regular int
			if type(value) is int:
				if -2147483648 < value < 2147483647:
					self._btwcode = value
				else:
					self._valueErrors["btwcode"] = ValueError("input voor btwcode is te groot / klein")
			else:
				self._valueErrors["btwcode"] = ValueError("input voor btwcode is ongeldig")

	@property
	def inbestelling(self):
		return self._inbestelling
	@inbestelling.setter
	def inbestelling(self, value):
		# Property CAN be None
		if value is None:
			self._inbestelling = value
		else:
			# smallint
			if type(value) is int:
				if -32768 < value < 32767:
					self._inbestelling = value
				else:
					self._valueErrors["inbestelling"] = ValueError("input voor inbestelling is te groot / klein")
			else:
				self._valueErrors["inbestelling"] = ValueError("input voor inbestelling is ongeldig")

	@property
	def bestelpunt(self):
		return self._bestelpunt
	@bestelpunt.setter
	def bestelpunt(self, value):
		# Property CAN be None
		if value is None:
			self._bestelpunt = value
		else:
			# smallint
			if type(value) is int:
				if -32768 < value < 32767:
					self._bestelpunt = value
				else:
					self._valueErrors["bestelpunt"] = ValueError("input voor bestelpunt is te groot / klein")
			else:
				self._valueErrors["bestelpunt"] = ValueError("input voor bestelpunt is ongeldig")

	@property
	def uitassortiment(self):
		return self._uitassortiment
	@uitassortiment.setter
	def uitassortiment(self, value):
		# Property CAN NOT be None
		# tinyint
		if type(value) is int:
			if -128 < value < 127:
				self._uitassortiment = value
			else:
				self._valueErrors["uitassortiment"] = ValueError("input voor uitassortiment is te groot / klein")
		else:
			self._valueErrors["uitassortiment"] = ValueError("input voor uitassortiment is ongeldig")

	def __str__(self):
		return "Producten: productnummer: %s" % self.productnummer

	def __repr__(self):
		self.__str__()
