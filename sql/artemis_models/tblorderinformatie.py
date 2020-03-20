import re


class tblorderinformatie:
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
		# Property CAN NOT be None
		# regular int
		if type(value) is int:
			if -2147483648 < value < 2147483647:
				self._orderid = value
			else:
				self._valueErrors["orderid"] = ValueError("input voor orderid is te groot / klein")
		else:
			self._valueErrors["orderid"] = ValueError("input voor orderid is ongeldig")

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
	def hoeveelheid(self):
		return self._hoeveelheid
	@hoeveelheid.setter
	def hoeveelheid(self, value):
		# Property CAN be None
		if value is None:
			self._hoeveelheid = value
		else:
			if type(value) is float:
				self._hoeveelheid = str(value)
			else:
				self._valueErrors["hoeveelheid"] = ValueError("input voor hoeveelheid is ongeldig")

	@property
	def korting(self):
		return self._korting
	@korting.setter
	def korting(self, value):
		# Property CAN be None
		if value is None:
			self._korting = value
		else:
			if type(value) is float:
				self._korting = str(value)
			else:
				self._valueErrors["korting"] = ValueError("input voor korting is ongeldig")

	def __str__(self):
		return "tblorderinformatie: orderid: %s" % self.orderid

	def __repr__(self):
		self.__str__()
