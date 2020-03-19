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
		if type(value) is int:
			self._orderid = value
		else:
			self._valueErrors["orderid"] = ValueError("input voor orderid is ongeldig")

	@property
	def klantnummer(self):
		return self._klantnummer
	@klantnummer.setter
	def klantnummer(self, value):
		if value is None:
			self._klantnummer = value
		else:
			self._klantnummer = str(value)

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
	def verzendid(self):
		return self._verzendid
	@verzendid.setter
	def verzendid(self, value):
		if value is None:
			self._verzendid = value
		else:
			self._verzendid = str(value)

	@property
	def orderdatum(self):
		return self._orderdatum
	@orderdatum.setter
	def orderdatum(self, value):
		if value is None:
			self._orderdatum = value
		else:
			if len(str(value)) <= 6:
				self._orderdatum = str(value)
			else:
				self._valueErrors["orderdatum"] = ValueError("input voor orderdatum is te lang")

	@property
	def vervaldatum(self):
		return self._vervaldatum
	@vervaldatum.setter
	def vervaldatum(self, value):
		if value is None:
			self._vervaldatum = value
		else:
			if len(str(value)) <= 6:
				self._vervaldatum = str(value)
			else:
				self._valueErrors["vervaldatum"] = ValueError("input voor vervaldatum is te lang")

	@property
	def leverdatum(self):
		return self._leverdatum
	@leverdatum.setter
	def leverdatum(self, value):
		if value is None:
			self._leverdatum = value
		else:
			if len(str(value)) <= 6:
				self._leverdatum = str(value)
			else:
				self._valueErrors["leverdatum"] = ValueError("input voor leverdatum is te lang")

	@property
	def vrachtkosten(self):
		return self._vrachtkosten
	@vrachtkosten.setter
	def vrachtkosten(self, value):
		if value is None:
			self._vrachtkosten = value
		else:
			self._vrachtkosten = str(value)

	def __str__(self):
		return "Orders: orderid: %s" % self.orderid

	def __repr__(self):
		self.__str__()
