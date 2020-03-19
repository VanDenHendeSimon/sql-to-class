class Categorieen:
	def __init__(self, categorienummer, categorienaam, bijschrijving):
		self._valueErrors = dict()
		self.categorienummer = categorienummer
		self.categorienaam = categorienaam
		self.bijschrijving = bijschrijving

	@property
	def valueErrors(self):
		return self._valueErrors

	@property
	def isValid(self):
		return len(self._valueErrors) == 0

	@property
	def categorienummer(self):
		return self._categorienummer
	@categorienummer.setter
	def categorienummer(self, value):
		if type(value) is int:
			self._categorienummer = value
		else:
			self._valueErrors["categorienummer"] = ValueError("input voor categorienummer is ongeldig")

	@property
	def categorienaam(self):
		return self._categorienaam
	@categorienaam.setter
	def categorienaam(self, value):
		if type(value) is str:
			if len(value) <= 20:
				self._categorienaam = value
			else:
				self._valueErrors["categorienaam"] = ValueError("input voor categorienaam is te lang")
		else:
			self._valueErrors["categorienaam"] = ValueError("input voor categorienaam is ongeldig")

	@property
	def bijschrijving(self):
		return self._bijschrijving
	@bijschrijving.setter
	def bijschrijving(self, value):
		if type(value) is str:
			if len(value) <= 50:
				self._bijschrijving = value
			else:
				self._valueErrors["bijschrijving"] = ValueError("input voor bijschrijving is te lang")
		else:
			self._valueErrors["bijschrijving"] = ValueError("input voor bijschrijving is ongeldig")

	def __str__(self):
		return "Categorieen: categorienummer: %s" % self.categorienummer

	def __repr__(self):
		self.__str__()
