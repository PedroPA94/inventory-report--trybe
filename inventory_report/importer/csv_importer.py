import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path_to_file: str) -> list:
        if not path_to_file.endswith('.csv'):
            raise ValueError('Arquivo inválido')

        with open(path_to_file, mode="r") as data:
            products = list(csv.DictReader(data))
            return products
