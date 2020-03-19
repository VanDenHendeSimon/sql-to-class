class Orderinformatie:
	def __init__(self, orderid, productnummer, hoeveelheid, korting):
		self._valueErrors = dict()
		self.orderid = orderid
		self.productnummer = productnummer
		self.hoeveelheid = hoeveelheid
		self.korting = korting

	@property
	def valueErrors(self):
		return self._valueErrors

	@property
	def isValid(self):
		return len(self._valueErrors) == 0

	@property
	def orderid(self):
		return self._orderid
	@orderid.setter
	def orderid(self, value):
		if type(value) is int:
			self._orderid = value
		else:
			self._valueErrors["orderid"] = ValueError("input voor orderid is ongeldig")

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
	def hoeveelheid(self):
		return self._hoeveelheid
	@hoeveelheid.setter
	def hoeveelheid(self, value):
		if value is None:
			self._hoeveelheid = value
		else:
			self._hoeveelheid = str(value)

	@property
	def korting(self):
		return self._korting
	@korting.setter
	def korting(self, value):
		if value is None:
			self._korting = value
		else:
			self._korting = str(value)

	def __str__(self):
		return "Orderinformatie: orderid: %s" % self.orderid

	def __repr__(self):
		self.__str__()
