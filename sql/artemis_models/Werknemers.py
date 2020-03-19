class Werknemers:
	def __init__(self, werknemerid, familienaam, voornaam, adres, gemeente, postcode, telefoonnummer, functie, brutowedde, superieur, toestelnummer, auto, indienst, geboortedatum, geslacht, foto, bijzonderheden):
		self._valueErrors = dict()
		self.werknemerid = werknemerid
		self.familienaam = familienaam
		self.voornaam = voornaam
		self.adres = adres
		self.gemeente = gemeente
		self.postcode = postcode
		self.telefoonnummer = telefoonnummer
		self.functie = functie
		self.brutowedde = brutowedde
		self.superieur = superieur
		self.toestelnummer = toestelnummer
		self.auto = auto
		self.indienst = indienst
		self.geboortedatum = geboortedatum
		self.geslacht = geslacht
		self.foto = foto
		self.bijzonderheden = bijzonderheden

	@property
	def valueErrors(self):
		return self._valueErrors

	@property
	def isValid(self):
		return len(self._valueErrors) == 0

	@property
	def werknemerid(self):
		return self._werknemerid
	@werknemerid.setter
	def werknemerid(self, value):
		if type(value) is int:
			self._werknemerid = value
		else:
			self._valueErrors["werknemerid"] = ValueError("input voor werknemerid is ongeldig")

	@property
	def familienaam(self):
		return self._familienaam
	@familienaam.setter
	def familienaam(self, value):
		if type(value) is str:
			if len(value) <= 40:
				self._familienaam = value
			else:
				self._valueErrors["familienaam"] = ValueError("input voor familienaam is te lang")
		else:
			self._valueErrors["familienaam"] = ValueError("input voor familienaam is ongeldig")

	@property
	def voornaam(self):
		return self._voornaam
	@voornaam.setter
	def voornaam(self, value):
		if value is None:
			self._voornaam = value
		else:
			if len(str(value)) <= 40:
				self._voornaam = str(value)
			else:
				self._valueErrors["voornaam"] = ValueError("input voor voornaam is te lang")

	@property
	def adres(self):
		return self._adres
	@adres.setter
	def adres(self, value):
		if value is None:
			self._adres = value
		else:
			if len(str(value)) <= 60:
				self._adres = str(value)
			else:
				self._valueErrors["adres"] = ValueError("input voor adres is te lang")

	@property
	def gemeente(self):
		return self._gemeente
	@gemeente.setter
	def gemeente(self, value):
		if value is None:
			self._gemeente = value
		else:
			if len(str(value)) <= 30:
				self._gemeente = str(value)
			else:
				self._valueErrors["gemeente"] = ValueError("input voor gemeente is te lang")

	@property
	def postcode(self):
		return self._postcode
	@postcode.setter
	def postcode(self, value):
		if value is None:
			self._postcode = value
		else:
			if len(str(value)) <= 4:
				self._postcode = str(value)
			else:
				self._valueErrors["postcode"] = ValueError("input voor postcode is te lang")

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

	@property
	def functie(self):
		return self._functie
	@functie.setter
	def functie(self, value):
		if value is None:
			self._functie = value
		else:
			if len(str(value)) <= 30:
				self._functie = str(value)
			else:
				self._valueErrors["functie"] = ValueError("input voor functie is te lang")

	@property
	def brutowedde(self):
		return self._brutowedde
	@brutowedde.setter
	def brutowedde(self, value):
		if value is None:
			self._brutowedde = value
		else:
			self._brutowedde = str(value)

	@property
	def superieur(self):
		return self._superieur
	@superieur.setter
	def superieur(self, value):
		if value is None:
			self._superieur = value
		else:
			if len(str(value)) <= 2:
				self._superieur = str(value)
			else:
				self._valueErrors["superieur"] = ValueError("input voor superieur is te lang")

	@property
	def toestelnummer(self):
		return self._toestelnummer
	@toestelnummer.setter
	def toestelnummer(self, value):
		if value is None:
			self._toestelnummer = value
		else:
			if len(str(value)) <= 2:
				self._toestelnummer = str(value)
			else:
				self._valueErrors["toestelnummer"] = ValueError("input voor toestelnummer is te lang")

	@property
	def auto(self):
		return self._auto
	@auto.setter
	def auto(self, value):

	@property
	def indienst(self):
		return self._indienst
	@indienst.setter
	def indienst(self, value):
		if value is None:
			self._indienst = value
		else:
			if len(str(value)) <= 6:
				self._indienst = str(value)
			else:
				self._valueErrors["indienst"] = ValueError("input voor indienst is te lang")

	@property
	def geboortedatum(self):
		return self._geboortedatum
	@geboortedatum.setter
	def geboortedatum(self, value):
		if value is None:
			self._geboortedatum = value
		else:
			if len(str(value)) <= 6:
				self._geboortedatum = str(value)
			else:
				self._valueErrors["geboortedatum"] = ValueError("input voor geboortedatum is te lang")

	@property
	def geslacht(self):
		return self._geslacht
	@geslacht.setter
	def geslacht(self, value):
		if value is None:
			self._geslacht = value
		else:
			if len(str(value)) <= 1:
				self._geslacht = str(value)
			else:
				self._valueErrors["geslacht"] = ValueError("input voor geslacht is te lang")

	@property
	def foto(self):
		return self._foto
	@foto.setter
	def foto(self, value):
		if value is None:
			self._foto = value
		else:
			self._foto = str(value)

	@property
	def bijzonderheden(self):
		return self._bijzonderheden
	@bijzonderheden.setter
	def bijzonderheden(self, value):
		if value is None:
			self._bijzonderheden = value
		else:
			self._bijzonderheden = str(value)

	def __str__(self):
		return "Werknemers: werknemerid: %s" % self.werknemerid

	def __repr__(self):
		self.__str__()
