import re


class Werknemertypes:
	def __init__(self, typeid, omschrijving):
		self._valueErrors = dict()
		self.typeid = typeid
		self.omschrijving = omschrijving

	@property
	def valueErrors(self):
		return self._valueErrors

	@property
	def isValid(self):
		return len(self._valueErrors) == 0

	@property
	def typeid(self):
		return self._typeid
	@typeid.setter
	def typeid(self, value):
		# Property CAN NOT be None
		# regular int
		if type(value) is int:
			if -2147483648 < value < 2147483647:
				self._typeid = value
			else:
				self._valueErrors["typeid"] = ValueError("input voor typeid is te groot / klein")
		else:
			self._valueErrors["typeid"] = ValueError("input voor typeid is ongeldig")

	@property
	def omschrijving(self):
		return self._omschrijving
	@omschrijving.setter
	def omschrijving(self, value):
		# Property CAN be None
		if value is None:
			self._omschrijving = value
		else:
			if type(value) is str:
				if len(str(value)) <= 50:
					self._omschrijving = str(value)
				else:
					self._valueErrors["omschrijving"] = ValueError("input voor omschrijving is te lang")
			else:
				self._valueErrors["omschrijving"] = ValueError("input voor omschrijving is ongeldig")

	def __str__(self):
		return "Werknemertypes: typeid: %s" % self.typeid

	def __repr__(self):
		self.__str__()
