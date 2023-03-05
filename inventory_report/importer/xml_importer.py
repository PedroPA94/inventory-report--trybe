import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path_to_file: str) -> list:
        if not path_to_file.endswith('.xml'):
            raise ValueError('Arquivo inválido')

        with open(path_to_file, mode="r") as data:
            tree = ET.parse(data)
            root = tree.getroot()
            records = [child for child in root]
            products = []

            for record in records:
                product = {}

                for child in record:
                    product[child.tag] = child.text
                products.append(product)

            return products
