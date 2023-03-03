from inventory_report.reports.simple_report import SimpleReport
from inventory_report.inventory.product import Product
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products: list[Product]) -> str:
        companies_counter = CompleteReport.get_companies_counter(products)

        return (
            f"{super().generate(products)}\n"
            "Produtos estocados por empresa:\n"
            f"{companies_counter}"
        )

    @classmethod
    def get_companies_counter(cls, products: list[Product]):
        companies = [
            product["nome_da_empresa"]
            for product in products
        ]

        companies_counter = Counter(companies)

        companies_string = ""

        for company, qty in companies_counter.items():
            companies_string += f"- {company}: {qty}\n"

        return companies_string
