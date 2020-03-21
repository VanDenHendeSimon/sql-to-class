import re


class Vlucht:
    def __init__(self, vluchtnr, vluchtdatum, bestemmingid, vliegtuigid):
        self._valueErrors = dict()
        self.vluchtnr = vluchtnr
        self.vluchtdatum = vluchtdatum
        self.bestemmingid = bestemmingid
        self.vliegtuigid = vliegtuigid

    @property
    def valueErrors(self):
        return self._valueErrors

    @property
    def isValid(self):
        return len(self._valueErrors) == 0

    @property
    def vluchtnr(self):
        return self._vluchtnr
    @vluchtnr.setter
    def vluchtnr(self, value):
        # Property CAN NOT be None
        # regular int
        if type(value) is int:
            if -2147483648 < value < 2147483647:
                self._vluchtnr = value
            else:
                self._valueErrors["vluchtnr"] = ValueError("input voor vluchtnr is te groot / klein")
        else:
            self._valueErrors["vluchtnr"] = ValueError("input voor vluchtnr is ongeldig")

    @property
    def vluchtdatum(self):
        return self._vluchtdatum
    @vluchtdatum.setter
    def vluchtdatum(self, value):
        # Property CAN be None
        if value is None:
            self._vluchtdatum = value
        else:
            if type(value) is str:
                if len(str(value)) <= 20:
                    self._vluchtdatum = str(value)
                else:
                    self._valueErrors["vluchtdatum"] = ValueError("input voor vluchtdatum is te lang")
            else:
                self._valueErrors["vluchtdatum"] = ValueError("input voor vluchtdatum is ongeldig")

    @property
    def bestemmingid(self):
        return self._bestemmingid
    @bestemmingid.setter
    def bestemmingid(self, value):
        # Property CAN be None
        if value is None:
            self._bestemmingid = value
        else:
            # regular int
            if type(value) is int:
                if -2147483648 < value < 2147483647:
                    self._bestemmingid = value
                else:
                    self._valueErrors["bestemmingid"] = ValueError("input voor bestemmingid is te groot / klein")
            else:
                self._valueErrors["bestemmingid"] = ValueError("input voor bestemmingid is ongeldig")

    @property
    def vliegtuigid(self):
        return self._vliegtuigid
    @vliegtuigid.setter
    def vliegtuigid(self, value):
        # Property CAN be None
        if value is None:
            self._vliegtuigid = value
        else:
            # regular int
            if type(value) is int:
                if -2147483648 < value < 2147483647:
                    self._vliegtuigid = value
                else:
                    self._valueErrors["vliegtuigid"] = ValueError("input voor vliegtuigid is te groot / klein")
            else:
                self._valueErrors["vliegtuigid"] = ValueError("input voor vliegtuigid is ongeldig")

    def __str__(self):
        return "Vlucht: vluchtnr: %s" % self.vluchtnr

    def __repr__(self):
        self.__str__()
