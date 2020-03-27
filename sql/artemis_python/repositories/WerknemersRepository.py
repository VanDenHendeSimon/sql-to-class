from models.Werknemers import Werknemers
from repositories.Database import Database


class WerknemersRepository:
    @staticmethod
    def json_or_formdata(request):
        """This function is only necessary when using the repo in the backend of an api"""
        if request.content_type == 'application/json':
            data = request.get_json()
        else:
            data = request.form.to_dict()

        return data

    @staticmethod
    def read_all():
        result = []
        sql = "SELECT * FROM artemis.tblwerknemers"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(WerknemersRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM artemis.tblwerknemers
        WHERE werknemerid = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Werknemers object
             result = WerknemersRepository.map_to_object(result)

        return result

    @staticmethod
    def check_column(row, column_name):
        result = None
        if column_name in row.keys() and row[column_name] is not None:
            result = row[column_name]

        return result

    @staticmethod
    def map_to_object(row):
        if row is not None and type(row) is dict:
            werknemerid = WerknemersRepository.check_column(row, "WerknemerID")
            werknemerid = int(werknemerid) if werknemerid is not None else None
            familienaam = WerknemersRepository.check_column(row, "Familienaam")
            voornaam = WerknemersRepository.check_column(row, "Voornaam")
            adres = WerknemersRepository.check_column(row, "Adres")
            gemeente = WerknemersRepository.check_column(row, "Gemeente")
            postcode = WerknemersRepository.check_column(row, "Postcode")
            telefoonnummer = WerknemersRepository.check_column(row, "Telefoonnummer")
            functie = WerknemersRepository.check_column(row, "Functie")
            brutowedde = WerknemersRepository.check_column(row, "BrutoWedde")
            brutowedde = int(brutowedde) if brutowedde is not None else None
            superieur = WerknemersRepository.check_column(row, "Superieur")
            toestelnummer = WerknemersRepository.check_column(row, "Toestelnummer")
            auto = WerknemersRepository.check_column(row, "Auto")
            auto = int(auto) if auto is not None else None
            indienst = WerknemersRepository.check_column(row, "InDienst")
            geboortedatum = WerknemersRepository.check_column(row, "Geboortedatum")
            geslacht = WerknemersRepository.check_column(row, "Geslacht")
            foto = WerknemersRepository.check_column(row, "Foto")
            foto = longblob(foto) if foto is not None else None
            bijzonderheden = WerknemersRepository.check_column(row, "Bijzonderheden")

        return Werknemers(werknemerid, familienaam, voornaam, adres, gemeente, postcode, telefoonnummer, functie, brutowedde, superieur, toestelnummer, auto, indienst, geboortedatum, geslacht, foto, bijzonderheden)
