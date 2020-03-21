import re


class Klant:
    def __init__(self, klantid, fnaam, vnaam, straat, nummer, postcode, gemeente):
        self._valueErrors = dict()
        self.klantid = klantid
        self.fnaam = fnaam
        self.vnaam = vnaam
        self.straat = straat
        self.nummer = nummer
        self.postcode = postcode
        self.gemeente = gemeente

    @property
    def valueErrors(self):
        return self._valueErrors

    @property
    def isValid(self):
        return len(self._valueErrors) == 0

    @property
    def klantid(self):
        return self._klantid
    @klantid.setter
    def klantid(self, value):
        # Property CAN NOT be None
        # regular int
        if type(value) is int:
            if -2147483648 < value < 2147483647:
                self._klantid = value
            else:
                self._valueErrors["klantid"] = ValueError("input voor klantid is te groot / klein")
        else:
            self._valueErrors["klantid"] = ValueError("input voor klantid is ongeldig")

    @property
    def fnaam(self):
        return self._fnaam
    @fnaam.setter
    def fnaam(self, value):
        # Property CAN be None
        if value is None:
            self._fnaam = value
        else:
            if type(value) is str:
                if len(str(value)) <= 50:
                    self._fnaam = str(value)
                else:
                    self._valueErrors["fnaam"] = ValueError("input voor fnaam is te lang")
            else:
                self._valueErrors["fnaam"] = ValueError("input voor fnaam is ongeldig")

    @property
    def vnaam(self):
        return self._vnaam
    @vnaam.setter
    def vnaam(self, value):
        # Property CAN be None
        if value is None:
            self._vnaam = value
        else:
            if type(value) is str:
                if len(str(value)) <= 50:
                    self._vnaam = str(value)
                else:
                    self._valueErrors["vnaam"] = ValueError("input voor vnaam is te lang")
            else:
                self._valueErrors["vnaam"] = ValueError("input voor vnaam is ongeldig")

    @property
    def straat(self):
        return self._straat
    @straat.setter
    def straat(self, value):
        # Property CAN be None
        if value is None:
            self._straat = value
        else:
            if type(value) is str:
                if len(str(value)) <= 50:
                    self._straat = str(value)
                else:
                    self._valueErrors["straat"] = ValueError("input voor straat is te lang")
            else:
                self._valueErrors["straat"] = ValueError("input voor straat is ongeldig")

    @property
    def nummer(self):
        return self._nummer
    @nummer.setter
    def nummer(self, value):
        # Property CAN be None
        if value is None:
            self._nummer = value
        else:
            if type(value) is str:
                if len(str(value)) <= 5:
                    self._nummer = str(value)
                else:
                    self._valueErrors["nummer"] = ValueError("input voor nummer is te lang")
            else:
                self._valueErrors["nummer"] = ValueError("input voor nummer is ongeldig")

    @property
    def postcode(self):
        return self._postcode
    @postcode.setter
    def postcode(self, value):
        # Property CAN be None
        if value is None:
            self._postcode = value
        else:
            # regular int
            if type(value) is int:
                if -2147483648 < value < 2147483647:
                    self._postcode = value
                else:
                    self._valueErrors["postcode"] = ValueError("input voor postcode is te groot / klein")
            else:
                self._valueErrors["postcode"] = ValueError("input voor postcode is ongeldig")

    @property
    def gemeente(self):
        return self._gemeente
    @gemeente.setter
    def gemeente(self, value):
        # Property CAN be None
        if value is None:
            self._gemeente = value
        else:
            if type(value) is str:
                if len(str(value)) <= 50:
                    self._gemeente = str(value)
                else:
                    self._valueErrors["gemeente"] = ValueError("input voor gemeente is te lang")
            else:
                self._valueErrors["gemeente"] = ValueError("input voor gemeente is ongeldig")

    def __str__(self):
        return "Klant: klantid: %s" % self.klantid

    def __repr__(self):
        self.__str__()
