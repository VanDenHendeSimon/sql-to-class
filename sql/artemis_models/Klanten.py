class Klanten:
	def __init__(self, klantnummer, naam, straat, postnr, gemeente, ondernemingsnr, klanten_type, saldo, opmerking):
		self._valueErrors = dict()
		self.klantnummer = klantnummer
		self.naam = naam
		self.straat = straat
		self.postnr = postnr
		self.gemeente = gemeente
		self.ondernemingsnr = ondernemingsnr
		self.klanten_type = klanten_type
		self.saldo = saldo
		self.opmerking = opmerking

	@property
	def valueErrors(self):
		return self._valueErrors

	@property
	def isValid(self):
		return len(self._valueErrors) == 0

	@property
	def klantnummer(self):
		return self._klantnummer
	@klantnummer.setter
	def klantnummer(self, value):
		if type(value) is int:
			self._klantnummer = value
		else:
			self._valueErrors["klantnummer"] = ValueError("input voor klantnummer is ongeldig")

	@property
	def naam(self):
		return self._naam
	@naam.setter
	def naam(self, value):
		if value is None:
			self._naam = value
		else:
			if len(str(value)) <= 50:
				self._naam = str(value)
			else:
				self._valueErrors["naam"] = ValueError("input voor naam is te lang")

	@property
	def straat(self):
		return self._straat
	@straat.setter
	def straat(self, value):
		if value is None:
			self._straat = value
		else:
			if len(str(value)) <= 50:
				self._straat = str(value)
			else:
				self._valueErrors["straat"] = ValueError("input voor straat is te lang")

	@property
	def postnr(self):
		return self._postnr
	@postnr.setter
	def postnr(self, value):
		if value is None:
			self._postnr = value
		else:
			if len(str(value)) <= 50:
				self._postnr = str(value)
			else:
				self._valueErrors["postnr"] = ValueError("input voor postnr is te lang")

	@property
	def gemeente(self):
		return self._gemeente
	@gemeente.setter
	def gemeente(self, value):
		if value is None:
			self._gemeente = value
		else:
			if len(str(value)) <= 50:
				self._gemeente = str(value)
			else:
				self._valueErrors["gemeente"] = ValueError("input voor gemeente is te lang")

	@property
	def ondernemingsnr(self):
		return self._ondernemingsnr
	@ondernemingsnr.setter
	def ondernemingsnr(self, value):
		if value is None:
			self._ondernemingsnr = value
		else:
			if len(str(value)) <= 50:
				self._ondernemingsnr = str(value)
			else:
				self._valueErrors["ondernemingsnr"] = ValueError("input voor ondernemingsnr is te lang")

	@property
	def klanten_type(self):
		return self._klanten_type
	@klanten_type.setter
	def klanten_type(self, value):
		if value is None:
			self._klanten_type = value
		else:
			if len(str(value)) <= 1:
				self._klanten_type = str(value)
			else:
				self._valueErrors["klanten_type"] = ValueError("input voor klanten_type is te lang")

	@property
	def saldo(self):
		return self._saldo
	@saldo.setter
	def saldo(self, value):
		if value is None:
			self._saldo = value
		else:
			self._saldo = str(value)

	@property
	def opmerking(self):
		return self._opmerking
	@opmerking.setter
	def opmerking(self, value):
		if value is None:
			self._opmerking = value
		else:
			self._opmerking = str(value)

	def __str__(self):
		return "Klanten: klantnummer: %s" % self.klantnummer

	def __repr__(self):
		self.__str__()
