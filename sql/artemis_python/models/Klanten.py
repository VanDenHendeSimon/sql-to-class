import re


class Klanten:
	def __init__(self, klantnummer, naam, straat, postnr, gemeente, ondernemingsnr, type_klanten, saldo, opmerking):
		self._valueErrors = dict()
		self.klantnummer = klantnummer
		self.naam = naam
		self.straat = straat
		self.postnr = postnr
		self.gemeente = gemeente
		self.ondernemingsnr = ondernemingsnr
		self.type_klanten = type_klanten
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
		# Property CAN NOT be None
		# regular int
		if type(value) is int:
			if -2147483648 < value < 2147483647:
				self._klantnummer = value
			else:
				self._valueErrors["klantnummer"] = ValueError("input voor klantnummer is te groot / klein")
		else:
			self._valueErrors["klantnummer"] = ValueError("input voor klantnummer is ongeldig")

	@property
	def naam(self):
		return self._naam
	@naam.setter
	def naam(self, value):
		# Property CAN be None
		if value is None:
			self._naam = value
		else:
			if type(value) is str:
				if len(str(value)) <= 50:
					self._naam = str(value)
				else:
					self._valueErrors["naam"] = ValueError("input voor naam is te lang")
			else:
				self._valueErrors["naam"] = ValueError("input voor naam is ongeldig")

	@property
	def straat(self):
		return self._straat
	@straat.setter
	def straat(self, value):
		# Property CAN be None
		if value is None:
			self._straat = value
		else:
			if type(value) is str:
				if len(str(value)) <= 50:
					self._straat = str(value)
				else:
					self._valueErrors["straat"] = ValueError("input voor straat is te lang")
			else:
				self._valueErrors["straat"] = ValueError("input voor straat is ongeldig")

	@property
	def postnr(self):
		return self._postnr
	@postnr.setter
	def postnr(self, value):
		# Property CAN be None
		if value is None:
			self._postnr = value
		else:
			if type(value) is str:
				if len(str(value)) <= 50:
					self._postnr = str(value)
				else:
					self._valueErrors["postnr"] = ValueError("input voor postnr is te lang")
			else:
				self._valueErrors["postnr"] = ValueError("input voor postnr is ongeldig")

	@property
	def gemeente(self):
		return self._gemeente
	@gemeente.setter
	def gemeente(self, value):
		# Property CAN be None
		if value is None:
			self._gemeente = value
		else:
			if type(value) is str:
				if len(str(value)) <= 50:
					self._gemeente = str(value)
				else:
					self._valueErrors["gemeente"] = ValueError("input voor gemeente is te lang")
			else:
				self._valueErrors["gemeente"] = ValueError("input voor gemeente is ongeldig")

	@property
	def ondernemingsnr(self):
		return self._ondernemingsnr
	@ondernemingsnr.setter
	def ondernemingsnr(self, value):
		# Property CAN be None
		if value is None:
			self._ondernemingsnr = value
		else:
			if type(value) is str:
				if len(str(value)) <= 50:
					self._ondernemingsnr = str(value)
				else:
					self._valueErrors["ondernemingsnr"] = ValueError("input voor ondernemingsnr is te lang")
			else:
				self._valueErrors["ondernemingsnr"] = ValueError("input voor ondernemingsnr is ongeldig")

	@property
	def type_klanten(self):
		return self._type_klanten
	@type_klanten.setter
	def type_klanten(self, value):
		# Property CAN be None
		if value is None:
			self._type_klanten = value
		else:
			if type(value) is str:
				if len(str(value)) <= 1:
					self._type_klanten = str(value)
				else:
					self._valueErrors["type_klanten"] = ValueError("input voor type_klanten is te lang")
			else:
				self._valueErrors["type_klanten"] = ValueError("input voor type_klanten is ongeldig")

	@property
	def saldo(self):
		return self._saldo
	@saldo.setter
	def saldo(self, value):
		# Property CAN be None
		if value is None:
			self._saldo = value
		else:
			if type(value) is float:
				self._saldo = str(value)
			else:
				self._valueErrors["saldo"] = ValueError("input voor saldo is ongeldig")

	@property
	def opmerking(self):
		return self._opmerking
	@opmerking.setter
	def opmerking(self, value):
		# Property CAN be None
		if value is None:
			self._opmerking = value
		else:
			if type(value) is str:
				self._opmerking = str(value)
			else:
				self._valueErrors["opmerking"] = ValueError("input voor opmerking is ongeldig")

	def __str__(self):
		return "Klanten: klantnummer: %s" % self.klantnummer

	def __repr__(self):
		self.__str__()
