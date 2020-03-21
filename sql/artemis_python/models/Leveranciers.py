import re


class Leveranciers:
    def __init__(self, leveranciersnummer, bedrijf, adres, plaats, postcode, land, url):
        self._valueErrors = dict()
        self.leveranciersnummer = leveranciersnummer
        self.bedrijf = bedrijf
        self.adres = adres
        self.plaats = plaats
        self.postcode = postcode
        self.land = land
        self.url = url

    @property
    def valueErrors(self):
        return self._valueErrors

    @property
    def isValid(self):
        return len(self._valueErrors) == 0

    @property
    def leveranciersnummer(self):
        return self._leveranciersnummer
    @leveranciersnummer.setter
    def leveranciersnummer(self, value):
        # Property CAN NOT be None
        # regular int
        if type(value) is int:
            if -2147483648 < value < 2147483647:
                self._leveranciersnummer = value
            else:
                self._valueErrors["leveranciersnummer"] = ValueError("input voor leveranciersnummer is te groot / klein")
        else:
            self._valueErrors["leveranciersnummer"] = ValueError("input voor leveranciersnummer is ongeldig")

    @property
    def bedrijf(self):
        return self._bedrijf
    @bedrijf.setter
    def bedrijf(self, value):
        # Property CAN be None
        if value is None:
            self._bedrijf = value
        else:
            if type(value) is str:
                if len(str(value)) <= 50:
                    self._bedrijf = str(value)
                else:
                    self._valueErrors["bedrijf"] = ValueError("input voor bedrijf is te lang")
            else:
                self._valueErrors["bedrijf"] = ValueError("input voor bedrijf is ongeldig")

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
                if len(str(value)) <= 50:
                    self._adres = str(value)
                else:
                    self._valueErrors["adres"] = ValueError("input voor adres is te lang")
            else:
                self._valueErrors["adres"] = ValueError("input voor adres is ongeldig")

    @property
    def plaats(self):
        return self._plaats
    @plaats.setter
    def plaats(self, value):
        # Property CAN be None
        if value is None:
            self._plaats = value
        else:
            if type(value) is str:
                if len(str(value)) <= 50:
                    self._plaats = str(value)
                else:
                    self._valueErrors["plaats"] = ValueError("input voor plaats is te lang")
            else:
                self._valueErrors["plaats"] = ValueError("input voor plaats is ongeldig")

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
                if len(str(value)) <= 50:
                    self._postcode = str(value)
                else:
                    self._valueErrors["postcode"] = ValueError("input voor postcode is te lang")
            else:
                self._valueErrors["postcode"] = ValueError("input voor postcode is ongeldig")

    @property
    def land(self):
        return self._land
    @land.setter
    def land(self, value):
        # Property CAN be None
        if value is None:
            self._land = value
        else:
            if type(value) is str:
                if len(str(value)) <= 50:
                    self._land = str(value)
                else:
                    self._valueErrors["land"] = ValueError("input voor land is te lang")
            else:
                self._valueErrors["land"] = ValueError("input voor land is ongeldig")

    @property
    def url(self):
        return self._url
    @url.setter
    def url(self, value):
        # Property CAN be None
        if value is None:
            self._url = value
        else:
            if type(value) is str:
                self._url = str(value)
            else:
                self._valueErrors["url"] = ValueError("input voor url is ongeldig")

    def __str__(self):
        return "Leveranciers: leveranciersnummer: %s" % self.leveranciersnummer

    def __repr__(self):
        self.__str__()
