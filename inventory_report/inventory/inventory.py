import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path_to_file: str, report_type: str) -> str:
        with open(path_to_file, mode="r") as data:
            if path_to_file.endswith('.csv'):
                products = list(csv.DictReader(data))
            elif path_to_file.endswith('.json'):
                products = json.load(data)
            else:
                tree = ET.parse(data)
                root = tree.getroot()
                records = [child for child in root]
                products = []
                for record in records:
                    product = {}
                    for child in record:
                        product[child.tag] = child.text
                    products.append(product)

            if report_type == 'simples':
                return SimpleReport.generate(products)

            return CompleteReport.generate(products)
