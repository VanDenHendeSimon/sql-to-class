import re


class Vliegtuig:
	def __init__(self, vliegtuigid, vliegtuigbouwer, type_vliegtuig, maxaantalzitplaatsenindittoestel, internecode):
		self._valueErrors = dict()
		self.vliegtuigid = vliegtuigid
		self.vliegtuigbouwer = vliegtuigbouwer
		self.type_vliegtuig = type_vliegtuig
		self.maxaantalzitplaatsenindittoestel = maxaantalzitplaatsenindittoestel
		self.internecode = internecode

	@property
	def valueErrors(self):
		return self._valueErrors

	@property
	def isValid(self):
		return len(self._valueErrors) == 0

	@property
	def vliegtuigid(self):
		return self._vliegtuigid
	@vliegtuigid.setter
	def vliegtuigid(self, value):
		# Property CAN NOT be None
		# regular int
		if type(value) is int:
			if -2147483648 < value < 2147483647:
				self._vliegtuigid = value
			else:
				self._valueErrors["vliegtuigid"] = ValueError("input voor vliegtuigid is te groot / klein")
		else:
			self._valueErrors["vliegtuigid"] = ValueError("input voor vliegtuigid is ongeldig")

	@property
	def vliegtuigbouwer(self):
		return self._vliegtuigbouwer
	@vliegtuigbouwer.setter
	def vliegtuigbouwer(self, value):
		# Property CAN be None
		if value is None:
			self._vliegtuigbouwer = value
		else:
			if type(value) is str:
				if len(str(value)) <= 50:
					self._vliegtuigbouwer = str(value)
				else:
					self._valueErrors["vliegtuigbouwer"] = ValueError("input voor vliegtuigbouwer is te lang")
			else:
				self._valueErrors["vliegtuigbouwer"] = ValueError("input voor vliegtuigbouwer is ongeldig")

	@property
	def type_vliegtuig(self):
		return self._type_vliegtuig
	@type_vliegtuig.setter
	def type_vliegtuig(self, value):
		# Property CAN be None
		if value is None:
			self._type_vliegtuig = value
		else:
			if type(value) is str:
				if len(str(value)) <= 50:
					self._type_vliegtuig = str(value)
				else:
					self._valueErrors["type_vliegtuig"] = ValueError("input voor type_vliegtuig is te lang")
			else:
				self._valueErrors["type_vliegtuig"] = ValueError("input voor type_vliegtuig is ongeldig")

	@property
	def maxaantalzitplaatsenindittoestel(self):
		return self._maxaantalzitplaatsenindittoestel
	@maxaantalzitplaatsenindittoestel.setter
	def maxaantalzitplaatsenindittoestel(self, value):
		# Property CAN be None
		if value is None:
			self._maxaantalzitplaatsenindittoestel = value
		else:
			# regular int
			if type(value) is int:
				if -2147483648 < value < 2147483647:
					self._maxaantalzitplaatsenindittoestel = value
				else:
					self._valueErrors["maxaantalzitplaatsenindittoestel"] = ValueError("input voor maxaantalzitplaatsenindittoestel is te groot / klein")
			else:
				self._valueErrors["maxaantalzitplaatsenindittoestel"] = ValueError("input voor maxaantalzitplaatsenindittoestel is ongeldig")

	@property
	def internecode(self):
		return self._internecode
	@internecode.setter
	def internecode(self, value):
		# Property CAN be None
		if value is None:
			self._internecode = value
		else:
			if type(value) is str:
				if len(str(value)) <= 50:
					self._internecode = str(value)
				else:
					self._valueErrors["internecode"] = ValueError("input voor internecode is te lang")
			else:
				self._valueErrors["internecode"] = ValueError("input voor internecode is ongeldig")

	def __str__(self):
		return "Vliegtuig: vliegtuigid: %s" % self.vliegtuigid

	def __repr__(self):
		self.__str__()
