import re


class Logins:
    def __init__(self, loginid, voornaam, naam, paswoord, gebdatum, login):
        self._valueErrors = dict()
        self.loginid = loginid
        self.voornaam = voornaam
        self.naam = naam
        self.paswoord = paswoord
        self.gebdatum = gebdatum
        self.login = login

    @property
    def valueErrors(self):
        return self._valueErrors

    @property
    def isValid(self):
        return len(self._valueErrors) == 0

    @property
    def loginid(self):
        return self._loginid
    @loginid.setter
    def loginid(self, value):
        # Property CAN NOT be None
        # regular int
        if type(value) is int:
            if -2147483648 < value < 2147483647:
                self._loginid = value
            else:
                self._valueErrors["loginid"] = ValueError("input voor loginid is te groot / klein")
        else:
            self._valueErrors["loginid"] = ValueError("input voor loginid is ongeldig")

    @property
    def voornaam(self):
        return self._voornaam
    @voornaam.setter
    def voornaam(self, value):
        # Property CAN NOT be None
        if type(value) is str:
            if len(str(value)) <= 7:
                self._voornaam = str(value)
            else:
                self._valueErrors["voornaam"] = ValueError("input voor voornaam is te lang")
        else:
            self._valueErrors["voornaam"] = ValueError("input voor voornaam is ongeldig")

    @property
    def naam(self):
        return self._naam
    @naam.setter
    def naam(self, value):
        # Property CAN NOT be None
        if type(value) is str:
            if len(str(value)) <= 8:
                self._naam = str(value)
            else:
                self._valueErrors["naam"] = ValueError("input voor naam is te lang")
        else:
            self._valueErrors["naam"] = ValueError("input voor naam is ongeldig")

    @property
    def paswoord(self):
        return self._paswoord
    @paswoord.setter
    def paswoord(self, value):
        # Property CAN NOT be None
        if type(value) is str:
            if len(str(value)) <= 45:
                self._paswoord = str(value)
            else:
                self._valueErrors["paswoord"] = ValueError("input voor paswoord is te lang")
        else:
            self._valueErrors["paswoord"] = ValueError("input voor paswoord is ongeldig")

    @property
    def gebdatum(self):
        return self._gebdatum
    @gebdatum.setter
    def gebdatum(self, value):
        # Property CAN NOT be None
        #'0000-00-00'
        if type(value) is str:
            try:
                if len(re.findall(r'\d{4}-\d{2}-\d{2}', value)[0]) == len(value):
                    self._gebdatum = str(value)
                else:
                    self._valueErrors["gebdatum"] = ValueError("input voor gebdatum match het patroon niet (yyyy-mm-dd)")
            except Exception:
                self._valueErrors["gebdatum"] = ValueError("input voor gebdatum match het patroon niet (yyyy-mm-dd)")
        else:
            self._valueErrors["gebdatum"] = ValueError("input voor gebdatum is ongeldig")

    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, value):
        # Property CAN NOT be None
        if type(value) is str:
            if len(str(value)) <= 9:
                self._login = str(value)
            else:
                self._valueErrors["login"] = ValueError("input voor login is te lang")
        else:
            self._valueErrors["login"] = ValueError("input voor login is ongeldig")

    def __str__(self):
        return "Logins: loginid: %s" % self.loginid

    def __repr__(self):
        self.__str__()
