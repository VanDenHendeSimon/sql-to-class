import re


class Bestemming:
    def __init__(self, bestemmingid, afkorting, voluit, land, typevlucht):
        self._valueErrors = dict()
        self.bestemmingid = bestemmingid
        self.afkorting = afkorting
        self.voluit = voluit
        self.land = land
        self.typevlucht = typevlucht

    @property
    def valueErrors(self):
        return self._valueErrors

    @property
    def isValid(self):
        return len(self._valueErrors) == 0

    @property
    def bestemmingid(self):
        return self._bestemmingid
    @bestemmingid.setter
    def bestemmingid(self, value):
        # Property CAN NOT be None
        # regular int
        if type(value) is int:
            if -2147483648 < value < 2147483647:
                self._bestemmingid = value
            else:
                self._valueErrors["bestemmingid"] = ValueError("input voor bestemmingid is te groot / klein")
        else:
            self._valueErrors["bestemmingid"] = ValueError("input voor bestemmingid is ongeldig")

    @property
    def afkorting(self):
        return self._afkorting
    @afkorting.setter
    def afkorting(self, value):
        # Property CAN be None
        if value is None:
            self._afkorting = value
        else:
            if type(value) is str:
                if len(str(value)) <= 3:
                    self._afkorting = str(value)
                else:
                    self._valueErrors["afkorting"] = ValueError("input voor afkorting is te lang")
            else:
                self._valueErrors["afkorting"] = ValueError("input voor afkorting is ongeldig")

    @property
    def voluit(self):
        return self._voluit
    @voluit.setter
    def voluit(self, value):
        # Property CAN be None
        if value is None:
            self._voluit = value
        else:
            if type(value) is str:
                if len(str(value)) <= 50:
                    self._voluit = str(value)
                else:
                    self._valueErrors["voluit"] = ValueError("input voor voluit is te lang")
            else:
                self._valueErrors["voluit"] = ValueError("input voor voluit is ongeldig")

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
    def typevlucht(self):
        return self._typevlucht
    @typevlucht.setter
    def typevlucht(self, value):
        # Property CAN be None
        if value is None:
            self._typevlucht = value
        else:
            # regular int
            if type(value) is int:
                if -2147483648 < value < 2147483647:
                    self._typevlucht = value
                else:
                    self._valueErrors["typevlucht"] = ValueError("input voor typevlucht is te groot / klein")
            else:
                self._valueErrors["typevlucht"] = ValueError("input voor typevlucht is ongeldig")

    def __str__(self):
        return "Bestemming: bestemmingid: %s" % self.bestemmingid

    def __repr__(self):
        self.__str__()
