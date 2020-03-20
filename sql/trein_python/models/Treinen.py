import re


class Treinen:
	def __init__(self, idtrein, vertrek, bestemmingid, spoor, vertraging, afgeschaft):
		self._valueErrors = dict()
		self.idtrein = idtrein
		self.vertrek = vertrek
		self.bestemmingid = bestemmingid
		self.spoor = spoor
		self.vertraging = vertraging
		self.afgeschaft = afgeschaft

	@property
	def valueErrors(self):
		return self._valueErrors

	@property
	def isValid(self):
		return len(self._valueErrors) == 0

	@property
	def idtrein(self):
		return self._idtrein
	@idtrein.setter
	def idtrein(self, value):
		# Property CAN NOT be None
		# regular int
		if type(value) is int:
			if -2147483648 < value < 2147483647:
				self._idtrein = value
			else:
				self._valueErrors["idtrein"] = ValueError("input voor idtrein is te groot / klein")
		else:
			self._valueErrors["idtrein"] = ValueError("input voor idtrein is ongeldig")

	@property
	def vertrek(self):
		return self._vertrek
	@vertrek.setter
	def vertrek(self, value):
		# Property CAN NOT be None
		if type(value) is tinytext:
			self._vertrek = str(value)
		else:
			self._valueErrors["vertrek"] = ValueError("input voor vertrek is ongeldig")

	@property
	def bestemmingid(self):
		return self._bestemmingid
	@bestemmingid.setter
	def bestemmingid(self, value):
		# Property CAN NOT be None
		# regular int
		if type(value) is int:
			if -2147483648 < value < 2147483647:
				self._bestemmingid = value
			else:
				self._valueErrors["bestemmingid"] = ValueError("input voor bestemmingid is te groot / klein")
		else:
			self._valueErrors["bestemmingid"] = ValueError("input voor bestemmingid is ongeldig")

	@property
	def spoor(self):
		return self._spoor
	@spoor.setter
	def spoor(self, value):
		# Property CAN NOT be None
		# regular int
		if type(value) is int:
			if -2147483648 < value < 2147483647:
				self._spoor = value
			else:
				self._valueErrors["spoor"] = ValueError("input voor spoor is te groot / klein")
		else:
			self._valueErrors["spoor"] = ValueError("input voor spoor is ongeldig")

	@property
	def vertraging(self):
		return self._vertraging
	@vertraging.setter
	def vertraging(self, value):
		# Property CAN be None
		if value is None:
			self._vertraging = value
		else:
			# regular int
			if type(value) is int:
				if -2147483648 < value < 2147483647:
					self._vertraging = value
				else:
					self._valueErrors["vertraging"] = ValueError("input voor vertraging is te groot / klein")
			else:
				self._valueErrors["vertraging"] = ValueError("input voor vertraging is ongeldig")

	@property
	def afgeschaft(self):
		return self._afgeschaft
	@afgeschaft.setter
	def afgeschaft(self, value):
		# Property CAN be None
		if value is None:
			self._afgeschaft = value
		else:
			# tinyint
			if type(value) is int:
				if -128 < value < 127:
					self._afgeschaft = value
				else:
					self._valueErrors["afgeschaft"] = ValueError("input voor afgeschaft is te groot / klein")
			else:
				self._valueErrors["afgeschaft"] = ValueError("input voor afgeschaft is ongeldig")

	def __str__(self):
		return "Treinen: idtrein: %s" % self.idtrein

	def __repr__(self):
		self.__str__()
