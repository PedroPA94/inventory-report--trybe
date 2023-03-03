import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path_to_file: str, report_type: str) -> str:
        with open(path_to_file, mode="r") as data:
            if path_to_file.endswith('.csv'):
                products = list(csv.DictReader(data))
            else:
                products = json.load(data)

            if report_type == 'simples':
                return SimpleReport.generate(products)

            return CompleteReport.generate(products)
