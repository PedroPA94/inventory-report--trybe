import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    try:
        _, path_to_file, report_type = sys.argv
    except ValueError:
        sys.stderr.write('Verifique os argumentos\n')
    else:
        importer = get_importer(path_to_file)
        inventory = InventoryRefactor(importer)
        report = inventory.import_data(path_to_file, report_type)
        sys.stdout.write(report)


def get_importer(path_to_file: str):
    if path_to_file.endswith('.csv'):
        return CsvImporter

    if path_to_file.endswith('.json'):
        return JsonImporter

    if path_to_file.endswith('.xml'):
        return XmlImporter

    raise ValueError('Arquivo inválido')
