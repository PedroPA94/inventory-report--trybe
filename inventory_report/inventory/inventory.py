import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path_to_file: str, report_type: str) -> str:
        with open(path_to_file, mode="r") as data:
            products = list(csv.DictReader(data))

            if report_type == 'simples':
                return SimpleReport.generate(products)

            return CompleteReport.generate(products)
