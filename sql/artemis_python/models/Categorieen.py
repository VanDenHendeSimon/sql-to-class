import re


class Categorieen:
    def __init__(self, categorienummer, categorienaam, bijschrijving):
        self._valueErrors = dict()
        self.categorienummer = categorienummer
        self.categorienaam = categorienaam
        self.bijschrijving = bijschrijving

    @property
    def valueErrors(self):
        return self._valueErrors

    @property
    def isValid(self):
        return len(self._valueErrors) == 0

    @property
    def categorienummer(self):
        return self._categorienummer
    @categorienummer.setter
    def categorienummer(self, value):
        # Property CAN NOT be None
        # regular int
        if type(value) is int:
            if -2147483648 < value < 2147483647:
                self._categorienummer = value
            else:
                self._valueErrors["categorienummer"] = ValueError("input voor categorienummer is te groot / klein")
        else:
            self._valueErrors["categorienummer"] = ValueError("input voor categorienummer is ongeldig")

    @property
    def categorienaam(self):
        return self._categorienaam
    @categorienaam.setter
    def categorienaam(self, value):
        # Property CAN NOT be None
        if type(value) is str:
            if len(str(value)) <= 20:
                self._categorienaam = str(value)
            else:
                self._valueErrors["categorienaam"] = ValueError("input voor categorienaam is te lang")
        else:
            self._valueErrors["categorienaam"] = ValueError("input voor categorienaam is ongeldig")

    @property
    def bijschrijving(self):
        return self._bijschrijving
    @bijschrijving.setter
    def bijschrijving(self, value):
        # Property CAN NOT be None
        if type(value) is str:
            if len(str(value)) <= 50:
                self._bijschrijving = str(value)
            else:
                self._valueErrors["bijschrijving"] = ValueError("input voor bijschrijving is te lang")
        else:
            self._valueErrors["bijschrijving"] = ValueError("input voor bijschrijving is ongeldig")

    def __str__(self):
        return "Categorieen: categorienummer: %s" % self.categorienummer

    def __repr__(self):
        self.__str__()
