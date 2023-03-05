import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path_to_file: str) -> list:
        if not path_to_file.endswith('.json'):
            raise ValueError('Arquivo inválido')

        with open(path_to_file, mode="r") as data:
            products = json.load(data)
            return products
