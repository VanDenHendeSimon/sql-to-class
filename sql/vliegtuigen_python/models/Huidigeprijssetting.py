import re


class Huidigeprijssetting:
    def __init__(self, typevlucht, huidigeprijssetting, omschrijving):
        self._valueErrors = dict()
        self.typevlucht = typevlucht
        self.huidigeprijssetting = huidigeprijssetting
        self.omschrijving = omschrijving

    @property
    def valueErrors(self):
        return self._valueErrors

    @property
    def isValid(self):
        return len(self._valueErrors) == 0

    @property
    def typevlucht(self):
        return self._typevlucht
    @typevlucht.setter
    def typevlucht(self, value):
        # Property CAN NOT be None
        # regular int
        if type(value) is int:
            if -2147483648 < value < 2147483647:
                self._typevlucht = value
            else:
                self._valueErrors["typevlucht"] = ValueError("input voor typevlucht is te groot / klein")
        else:
            self._valueErrors["typevlucht"] = ValueError("input voor typevlucht is ongeldig")

    @property
    def huidigeprijssetting(self):
        return self._huidigeprijssetting
    @huidigeprijssetting.setter
    def huidigeprijssetting(self, value):
        # Property CAN be None
        if value is None:
            self._huidigeprijssetting = value
        else:
            if type(value) is float:
                if "." in str(value):
                    if ((len(str(value).split(".")[0]) <= 16) and (len(str(value).split(".")[1]) <= 2)):
                        self._huidigeprijssetting = value
                    else:
                        self._valueErrors["huidigeprijssetting"] = ValueError("input voor huidigeprijssetting is te groot / klein")
                else:
                    if len(str(value)) <= 18:
                        self._huidigeprijssetting = value
                    else:
                        self._valueErrors["huidigeprijssetting"] = ValueError("input voor huidigeprijssetting is te lang")
            else:
                self._valueErrors["huidigeprijssetting"] = ValueError("input voor huidigeprijssetting is ongeldig")

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
        return "Huidigeprijssetting: typevlucht: %s" % self.typevlucht

    def __repr__(self):
        self.__str__()
