import re


class Btwtarief:
	def __init__(self, btwcode, btwpercentage):
		self._valueErrors = dict()
		self.btwcode = btwcode
		self.btwpercentage = btwpercentage

	@property
	def valueErrors(self):
		return self._valueErrors

	@property
	def isValid(self):
		return len(self._valueErrors) == 0

	@property
	def btwcode(self):
		return self._btwcode
	@btwcode.setter
	def btwcode(self, value):
		# Property CAN NOT be None
		# regular int
		if type(value) is int:
			if -2147483648 < value < 2147483647:
				self._btwcode = value
			else:
				self._valueErrors["btwcode"] = ValueError("input voor btwcode is te groot / klein")
		else:
			self._valueErrors["btwcode"] = ValueError("input voor btwcode is ongeldig")

	@property
	def btwpercentage(self):
		return self._btwpercentage
	@btwpercentage.setter
	def btwpercentage(self, value):
		# Property CAN be None
		if value is None:
			self._btwpercentage = value
		else:
			if type(value) is float:
				if "." in str(value):
					if ((len(str(value).split(".")[0]) <= 8) and (len(str(value).split(".")[1]) <= 2)):
						self._btwpercentage = value
					else:
						self._valueErrors["btwpercentage"] = ValueError("input voor btwpercentage is te groot / klein")
				else:
					if len(str(value)) <= 10:
						self._btwpercentage = value
					else:
						self._valueErrors["btwpercentage"] = ValueError("input voor btwpercentage is te lang")
			else:
				self._valueErrors["btwpercentage"] = ValueError("input voor btwpercentage is ongeldig")

	def __str__(self):
		return "Btwtarief: btwcode: %s" % self.btwcode

	def __repr__(self):
		self.__str__()
