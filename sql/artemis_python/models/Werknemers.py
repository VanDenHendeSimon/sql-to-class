import re


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
		# Property CAN NOT be None
		# regular int
		if type(value) is int:
			if -2147483648 < value < 2147483647:
				self._werknemerid = value
			else:
				self._valueErrors["werknemerid"] = ValueError("input voor werknemerid is te groot / klein")
		else:
			self._valueErrors["werknemerid"] = ValueError("input voor werknemerid is ongeldig")

	@property
	def familienaam(self):
		return self._familienaam
	@familienaam.setter
	def familienaam(self, value):
		# Property CAN NOT be None
		if type(value) is str:
			if len(str(value)) <= 40:
				self._familienaam = str(value)
			else:
				self._valueErrors["familienaam"] = ValueError("input voor familienaam is te lang")
		else:
			self._valueErrors["familienaam"] = ValueError("input voor familienaam is ongeldig")

	@property
	def voornaam(self):
		return self._voornaam
	@voornaam.setter
	def voornaam(self, value):
		# Property CAN be None
		if value is None:
			self._voornaam = value
		else:
			if type(value) is str:
				if len(str(value)) <= 40:
					self._voornaam = str(value)
				else:
					self._valueErrors["voornaam"] = ValueError("input voor voornaam is te lang")
			else:
				self._valueErrors["voornaam"] = ValueError("input voor voornaam is ongeldig")

	@property
	def adres(self):
		return self._adres
	@adres.setter
	def adres(self, value):
		# Property CAN be None
		if value is None:
			self._adres = value
		else:
			if type(value) is str:
				if len(str(value)) <= 60:
					self._adres = str(value)
				else:
					self._valueErrors["adres"] = ValueError("input voor adres is te lang")
			else:
				self._valueErrors["adres"] = ValueError("input voor adres is ongeldig")

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
				if len(str(value)) <= 30:
					self._gemeente = str(value)
				else:
					self._valueErrors["gemeente"] = ValueError("input voor gemeente is te lang")
			else:
				self._valueErrors["gemeente"] = ValueError("input voor gemeente is ongeldig")

	@property
	def postcode(self):
		return self._postcode
	@postcode.setter
	def postcode(self, value):
		# Property CAN be None
		if value is None:
			self._postcode = value
		else:
			if type(value) is str:
				if len(str(value)) <= 4:
					self._postcode = str(value)
				else:
					self._valueErrors["postcode"] = ValueError("input voor postcode is te lang")
			else:
				self._valueErrors["postcode"] = ValueError("input voor postcode is ongeldig")

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

	@property
	def functie(self):
		return self._functie
	@functie.setter
	def functie(self, value):
		# Property CAN be None
		if value is None:
			self._functie = value
		else:
			if type(value) is str:
				if len(str(value)) <= 30:
					self._functie = str(value)
				else:
					self._valueErrors["functie"] = ValueError("input voor functie is te lang")
			else:
				self._valueErrors["functie"] = ValueError("input voor functie is ongeldig")

	@property
	def brutowedde(self):
		return self._brutowedde
	@brutowedde.setter
	def brutowedde(self, value):
		# Property CAN be None
		if value is None:
			self._brutowedde = value
		else:
			# regular int
			if type(value) is int:
				if -2147483648 < value < 2147483647:
					self._brutowedde = value
				else:
					self._valueErrors["brutowedde"] = ValueError("input voor brutowedde is te groot / klein")
			else:
				self._valueErrors["brutowedde"] = ValueError("input voor brutowedde is ongeldig")

	@property
	def superieur(self):
		return self._superieur
	@superieur.setter
	def superieur(self, value):
		# Property CAN be None
		if value is None:
			self._superieur = value
		else:
			if type(value) is str:
				if len(str(value)) <= 2:
					self._superieur = str(value)
				else:
					self._valueErrors["superieur"] = ValueError("input voor superieur is te lang")
			else:
				self._valueErrors["superieur"] = ValueError("input voor superieur is ongeldig")

	@property
	def toestelnummer(self):
		return self._toestelnummer
	@toestelnummer.setter
	def toestelnummer(self, value):
		# Property CAN be None
		if value is None:
			self._toestelnummer = value
		else:
			if type(value) is str:
				if len(str(value)) <= 2:
					self._toestelnummer = str(value)
				else:
					self._valueErrors["toestelnummer"] = ValueError("input voor toestelnummer is te lang")
			else:
				self._valueErrors["toestelnummer"] = ValueError("input voor toestelnummer is ongeldig")

	@property
	def auto(self):
		return self._auto
	@auto.setter
	def auto(self, value):
		# Property CAN NOT be None
		# tinyint
		if type(value) is int:
			if -128 < value < 127:
				self._auto = value
			else:
				self._valueErrors["auto"] = ValueError("input voor auto is te groot / klein")
		else:
			self._valueErrors["auto"] = ValueError("input voor auto is ongeldig")

	@property
	def indienst(self):
		return self._indienst
	@indienst.setter
	def indienst(self, value):
		# Property CAN be None
		if value is None:
			self._indienst = value
		else:
			#'0000-00-00 00:00:00'
			if type(value) is str:
				try:
					if len(re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', value)[0]) == len(value):
						self._indienst = str(value)
					else:
						self._valueErrors["indienst"] = ValueError("input voor indienst match het patroon niet (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")
				except Exception:
					self._valueErrors["indienst"] = ValueError("input voor indienst match het patroon niet (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")
			else:
				self._valueErrors["indienst"] = ValueError("input voor indienst is ongeldig")

	@property
	def geboortedatum(self):
		return self._geboortedatum
	@geboortedatum.setter
	def geboortedatum(self, value):
		# Property CAN be None
		if value is None:
			self._geboortedatum = value
		else:
			#'0000-00-00 00:00:00'
			if type(value) is str:
				try:
					if len(re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', value)[0]) == len(value):
						self._geboortedatum = str(value)
					else:
						self._valueErrors["geboortedatum"] = ValueError("input voor geboortedatum match het patroon niet (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")
				except Exception:
					self._valueErrors["geboortedatum"] = ValueError("input voor geboortedatum match het patroon niet (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")
			else:
				self._valueErrors["geboortedatum"] = ValueError("input voor geboortedatum is ongeldig")

	@property
	def geslacht(self):
		return self._geslacht
	@geslacht.setter
	def geslacht(self, value):
		# Property CAN be None
		if value is None:
			self._geslacht = value
		else:
			if type(value) is str:
				if len(str(value)) <= 1:
					self._geslacht = str(value)
				else:
					self._valueErrors["geslacht"] = ValueError("input voor geslacht is te lang")
			else:
				self._valueErrors["geslacht"] = ValueError("input voor geslacht is ongeldig")

	@property
	def foto(self):
		return self._foto
	@foto.setter
	def foto(self, value):
		# Property CAN be None
		if value is None:
			self._foto = value
		else:
			if type(value) is longblob:
				self._foto = str(value)
			else:
				self._valueErrors["foto"] = ValueError("input voor foto is ongeldig")

	@property
	def bijzonderheden(self):
		return self._bijzonderheden
	@bijzonderheden.setter
	def bijzonderheden(self, value):
		# Property CAN be None
		if value is None:
			self._bijzonderheden = value
		else:
			if type(value) is str:
				self._bijzonderheden = str(value)
			else:
				self._valueErrors["bijzonderheden"] = ValueError("input voor bijzonderheden is ongeldig")

	def __str__(self):
		return "Werknemers: werknemerid: %s" % self.werknemerid

	def __repr__(self):
		self.__str__()
