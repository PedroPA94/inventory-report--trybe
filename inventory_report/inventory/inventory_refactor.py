from collections.abc import Iterable
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = []

    def import_data(self, path_to_file: str, report_type: str) -> str:
        data = self.importer.import_data(path_to_file)
        self.data += data

        if report_type == 'simples':
            return SimpleReport.generate(data)

        return CompleteReport.generate(data)

    def __iter__(self):
        return InventoryIterator(self.data)
