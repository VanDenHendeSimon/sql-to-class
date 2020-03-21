import re


class Werknemer:
    def __init__(self, werknemerid, naam, typeid, foto):
        self._valueErrors = dict()
        self.werknemerid = werknemerid
        self.naam = naam
        self.typeid = typeid
        self.foto = foto

    @property
    def valueErrors(self):
        return self._valueErrors

    @property
    def isValid(self):
        return len(self._valueErrors) == 0

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
    def naam(self):
        return self._naam
    @naam.setter
    def naam(self, value):
        # Property CAN be None
        if value is None:
            self._naam = value
        else:
            if type(value) is str:
                if len(str(value)) <= 50:
                    self._naam = str(value)
                else:
                    self._valueErrors["naam"] = ValueError("input voor naam is te lang")
            else:
                self._valueErrors["naam"] = ValueError("input voor naam is ongeldig")

    @property
    def typeid(self):
        return self._typeid
    @typeid.setter
    def typeid(self, value):
        # Property CAN be None
        if value is None:
            self._typeid = value
        else:
            # regular int
            if type(value) is int:
                if -2147483648 < value < 2147483647:
                    self._typeid = value
                else:
                    self._valueErrors["typeid"] = ValueError("input voor typeid is te groot / klein")
            else:
                self._valueErrors["typeid"] = ValueError("input voor typeid is ongeldig")

    @property
    def foto(self):
        return self._foto
    @foto.setter
    def foto(self, value):
        # Property CAN NOT be None
        if type(value) is str:
            if len(str(value)) <= 255:
                self._foto = str(value)
            else:
                self._valueErrors["foto"] = ValueError("input voor foto is te lang")
        else:
            self._valueErrors["foto"] = ValueError("input voor foto is ongeldig")

    def __str__(self):
        return "Werknemer: werknemerid: %s" % self.werknemerid

    def __repr__(self):
        self.__str__()
