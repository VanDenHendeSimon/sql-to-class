import re


class Bestemmingen:
    def __init__(self, idbestemming, stad, latitude, llngitude):
        self._valueErrors = dict()
        self.idbestemming = idbestemming
        self.stad = stad
        self.latitude = latitude
        self.llngitude = llngitude

    @property
    def valueErrors(self):
        return self._valueErrors

    @property
    def isValid(self):
        return len(self._valueErrors) == 0

    @property
    def idbestemming(self):
        return self._idbestemming
    @idbestemming.setter
    def idbestemming(self, value):
        # Property CAN NOT be None
        # regular int
        if type(value) is int:
            if -2147483648 < value < 2147483647:
                self._idbestemming = value
            else:
                self._valueErrors["idbestemming"] = ValueError("input voor idbestemming is te groot / klein")
        else:
            self._valueErrors["idbestemming"] = ValueError("input voor idbestemming is ongeldig")

    @property
    def stad(self):
        return self._stad
    @stad.setter
    def stad(self, value):
        # Property CAN NOT be None
        if type(value) is str:
            if len(str(value)) <= 45:
                self._stad = str(value)
            else:
                self._valueErrors["stad"] = ValueError("input voor stad is te lang")
        else:
            self._valueErrors["stad"] = ValueError("input voor stad is ongeldig")

    @property
    def latitude(self):
        return self._latitude
    @latitude.setter
    def latitude(self, value):
        # Property CAN NOT be None
        if type(value) is str:
            if len(str(value)) <= 10:
                self._latitude = str(value)
            else:
                self._valueErrors["latitude"] = ValueError("input voor latitude is te lang")
        else:
            self._valueErrors["latitude"] = ValueError("input voor latitude is ongeldig")

    @property
    def llngitude(self):
        return self._llngitude
    @llngitude.setter
    def llngitude(self, value):
        # Property CAN NOT be None
        if type(value) is str:
            if len(str(value)) <= 10:
                self._llngitude = str(value)
            else:
                self._valueErrors["llngitude"] = ValueError("input voor llngitude is te lang")
        else:
            self._valueErrors["llngitude"] = ValueError("input voor llngitude is ongeldig")

    def __str__(self):
        return "Bestemmingen: idbestemming: %s" % self.idbestemming

    def __repr__(self):
        self.__str__()
