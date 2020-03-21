import re


class Orders:
	def __init__(self, orderid, klantnummer, werknemerid, verzendid, orderdatum, vervaldatum, leverdatum, vrachtkosten):
		self._valueErrors = dict()
		self.orderid = orderid
		self.klantnummer = klantnummer
		self.werknemerid = werknemerid
		self.verzendid = verzendid
		self.orderdatum = orderdatum
		self.vervaldatum = vervaldatum
		self.leverdatum = leverdatum
		self.vrachtkosten = vrachtkosten

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
	def klantnummer(self):
		return self._klantnummer
	@klantnummer.setter
	def klantnummer(self, value):
		# Property CAN be None
		if value is None:
			self._klantnummer = value
		else:
			# regular int
			if type(value) is int:
				if -2147483648 < value < 2147483647:
					self._klantnummer = value
				else:
					self._valueErrors["klantnummer"] = ValueError("input voor klantnummer is te groot / klein")
			else:
				self._valueErrors["klantnummer"] = ValueError("input voor klantnummer is ongeldig")

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
	def verzendid(self):
		return self._verzendid
	@verzendid.setter
	def verzendid(self, value):
		# Property CAN be None
		if value is None:
			self._verzendid = value
		else:
			# smallint
			if type(value) is int:
				if -32768 < value < 32767:
					self._verzendid = value
				else:
					self._valueErrors["verzendid"] = ValueError("input voor verzendid is te groot / klein")
			else:
				self._valueErrors["verzendid"] = ValueError("input voor verzendid is ongeldig")

	@property
	def orderdatum(self):
		return self._orderdatum
	@orderdatum.setter
	def orderdatum(self, value):
		# Property CAN be None
		if value is None:
			self._orderdatum = value
		else:
			#'0000-00-00 00:00:00'
			if type(value) is str:
				try:
					if len(re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', value)[0]) == len(value):
						self._orderdatum = str(value)
					else:
						self._valueErrors["orderdatum"] = ValueError("input voor orderdatum match het patroon niet (yyyy-mm-dd hh:mm:ss)")
				except Exception:
					self._valueErrors["orderdatum"] = ValueError("input voor orderdatum match het patroon niet (yyyy-mm-dd hh:mm:ss)")
			else:
				self._valueErrors["orderdatum"] = ValueError("input voor orderdatum is ongeldig")

	@property
	def vervaldatum(self):
		return self._vervaldatum
	@vervaldatum.setter
	def vervaldatum(self, value):
		# Property CAN be None
		if value is None:
			self._vervaldatum = value
		else:
			#'0000-00-00 00:00:00'
			if type(value) is str:
				try:
					if len(re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', value)[0]) == len(value):
						self._vervaldatum = str(value)
					else:
						self._valueErrors["vervaldatum"] = ValueError("input voor vervaldatum match het patroon niet (yyyy-mm-dd hh:mm:ss)")
				except Exception:
					self._valueErrors["vervaldatum"] = ValueError("input voor vervaldatum match het patroon niet (yyyy-mm-dd hh:mm:ss)")
			else:
				self._valueErrors["vervaldatum"] = ValueError("input voor vervaldatum is ongeldig")

	@property
	def leverdatum(self):
		return self._leverdatum
	@leverdatum.setter
	def leverdatum(self, value):
		# Property CAN be None
		if value is None:
			self._leverdatum = value
		else:
			#'0000-00-00 00:00:00'
			if type(value) is str:
				try:
					if len(re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', value)[0]) == len(value):
						self._leverdatum = str(value)
					else:
						self._valueErrors["leverdatum"] = ValueError("input voor leverdatum match het patroon niet (yyyy-mm-dd hh:mm:ss)")
				except Exception:
					self._valueErrors["leverdatum"] = ValueError("input voor leverdatum match het patroon niet (yyyy-mm-dd hh:mm:ss)")
			else:
				self._valueErrors["leverdatum"] = ValueError("input voor leverdatum is ongeldig")

	@property
	def vrachtkosten(self):
		return self._vrachtkosten
	@vrachtkosten.setter
	def vrachtkosten(self, value):
		# Property CAN be None
		if value is None:
			self._vrachtkosten = value
		else:
			if type(value) is float:
				self._vrachtkosten = str(value)
			else:
				self._valueErrors["vrachtkosten"] = ValueError("input voor vrachtkosten is ongeldig")

	def __str__(self):
		return "Orders: orderid: %s" % self.orderid

	def __repr__(self):
		self.__str__()
