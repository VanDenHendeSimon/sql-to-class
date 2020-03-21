from models.Producten import Producten
from repositories.Database import Database


class ProductenRepository:
    @ staticmethod
    def read_all():
        result = []
        sql = "SELECT * FROM artemis.tblproducten"
        rows = Database.get_rows(sql)

        if rows is not None:
            for row in rows:
                # mapping naar object
                result.append(ProductenRepository.map_to_object(row))

        return result

    @staticmethod
    def read_single(_id):
        if not _id:
            return "Ongedlig ID. Probeer opnieuw"

        sql = """
        SELECT
            *
        FROM artemis.tblproducten
        WHERE productnummer = %s
        """
        params = [_id]

        result = Database.get_one_row(sql, params)

        if type(result) is dict:
            # Mapping naar Producten object
             result = ProductenRepository.map_to_object(result)

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
            productnummer = ProductenRepository.check_column(row, "Productnummer")
            productnummer = int(productnummer) if productnummer is not None else None

            leveranciersnummer = ProductenRepository.check_column(row, "Leveranciersnummer")
            leveranciersnummer = int(leveranciersnummer) if leveranciersnummer is not None else None

            categorienummer = ProductenRepository.check_column(row, "Categorienummer")
            categorienummer = int(categorienummer) if categorienummer is not None else None

            productnaam = ProductenRepository.check_column(row, "Productnaam")
            nederlandsenaam = ProductenRepository.check_column(row, "NederlandseNaam")
            hoeveelheidpereenheid = ProductenRepository.check_column(row, "HoeveelheidPerEenheid")
            prijspereenheid = ProductenRepository.check_column(row, "PrijsPerEenheid")
            prijspereenheid = float(prijspereenheid) if prijspereenheid is not None else None

            voorraad = ProductenRepository.check_column(row, "Voorraad")
            voorraad = int(voorraad) if voorraad is not None else None

            btwcode = ProductenRepository.check_column(row, "BTWCode")
            btwcode = int(btwcode) if btwcode is not None else None

            inbestelling = ProductenRepository.check_column(row, "InBestelling")
            inbestelling = int(inbestelling) if inbestelling is not None else None

            bestelpunt = ProductenRepository.check_column(row, "Bestelpunt")
            bestelpunt = int(bestelpunt) if bestelpunt is not None else None

            uitassortiment = ProductenRepository.check_column(row, "UitAssortiment")
            uitassortiment = int(uitassortiment) if uitassortiment is not None else None


        return Producten(productnummer, leveranciersnummer, categorienummer, productnaam, nederlandsenaam, hoeveelheidpereenheid, prijspereenheid, voorraad, btwcode, inbestelling, bestelpunt, uitassortiment)
