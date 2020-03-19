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
		if type(value) is int:
			self._btwcode = value
		else:
			self._valueErrors["btwcode"] = ValueError("input voor btwcode is ongeldig")

	@property
	def btwpercentage(self):
		return self._btwpercentage
	@btwpercentage.setter
	def btwpercentage(self, value):
		if value is None:
			self._btwpercentage = value
		else:
			if "." in str(value):
				if ((len(str(value).split(".")[0]) <= 8) and (len(str(value).split(".")[1]) <= 2)):
					self._btwpercentage = value
				else:
					self._valueErrors["btwpercentage"] = ValueError("input voor btwpercentage is te lang")
			else:
				if len(str(value)) <= 10:
					self._btwpercentage = value
				else:
					self._valueErrors["btwpercentage"] = ValueError("input voor btwpercentage is te lang")

	def __str__(self):
		return "Btwtarief: btwcode: %s" % self.btwcode

	def __repr__(self):
		self.__str__()
