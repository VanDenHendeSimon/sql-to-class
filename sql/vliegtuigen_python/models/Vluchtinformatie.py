import re


class Vluchtinformatie:
    def __init__(self, vluchtnr, stoelnr, klantid, prijsbetaaldvoorstoel):
        self._valueErrors = dict()
        self.vluchtnr = vluchtnr
        self.stoelnr = stoelnr
        self.klantid = klantid
        self.prijsbetaaldvoorstoel = prijsbetaaldvoorstoel

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
    def stoelnr(self):
        return self._stoelnr
    @stoelnr.setter
    def stoelnr(self, value):
        # Property CAN NOT be None
        # regular int
        if type(value) is int:
            if -2147483648 < value < 2147483647:
                self._stoelnr = value
            else:
                self._valueErrors["stoelnr"] = ValueError("input voor stoelnr is te groot / klein")
        else:
            self._valueErrors["stoelnr"] = ValueError("input voor stoelnr is ongeldig")

    @property
    def klantid(self):
        return self._klantid
    @klantid.setter
    def klantid(self, value):
        # Property CAN be None
        if value is None:
            self._klantid = value
        else:
            # regular int
            if type(value) is int:
                if -2147483648 < value < 2147483647:
                    self._klantid = value
                else:
                    self._valueErrors["klantid"] = ValueError("input voor klantid is te groot / klein")
            else:
                self._valueErrors["klantid"] = ValueError("input voor klantid is ongeldig")

    @property
    def prijsbetaaldvoorstoel(self):
        return self._prijsbetaaldvoorstoel
    @prijsbetaaldvoorstoel.setter
    def prijsbetaaldvoorstoel(self, value):
        # Property CAN be None
        if value is None:
            self._prijsbetaaldvoorstoel = value
        else:
            if type(value) is float:
                if "." in str(value):
                    if ((len(str(value).split(".")[0]) <= 16) and (len(str(value).split(".")[1]) <= 2)):
                        self._prijsbetaaldvoorstoel = value
                    else:
                        self._valueErrors["prijsbetaaldvoorstoel"] = ValueError("input voor prijsbetaaldvoorstoel is te groot / klein")
                else:
                    if len(str(value)) <= 18:
                        self._prijsbetaaldvoorstoel = value
                    else:
                        self._valueErrors["prijsbetaaldvoorstoel"] = ValueError("input voor prijsbetaaldvoorstoel is te lang")
            else:
                self._valueErrors["prijsbetaaldvoorstoel"] = ValueError("input voor prijsbetaaldvoorstoel is ongeldig")

    def __str__(self):
        return "Vluchtinformatie: vluchtnr: %s" % self.vluchtnr

    def __repr__(self):
        self.__str__()
