from inventory_report.reports.report import Report
from inventory_report.inventory.product import Product
from datetime import datetime
from collections import Counter


class SimpleReport(Report):
    @classmethod
    def generate(cls, products: list[Product]) -> str:
        oldest_product_date = SimpleReport.get_oldest_product_date(products)
        nearest_exp_date = SimpleReport.get_nearest_expiration_date(products)
        highest_count_co = SimpleReport.get_highest_count_co(products)

        return (
            f"Data de fabricação mais antiga: {oldest_product_date}\n"
            f"Data de validade mais próxima: {nearest_exp_date}\n"
            f"Empresa com mais produtos: {highest_count_co}"
        )
    @classmethod
    def get_oldest_product_date(cls, products: list[Product]) -> str:
        dates = [
            datetime.strptime(product["data_de_fabricacao"], "%Y-%m-%d")
            for product in products
        ]

        oldest_date = min(dates)
        return oldest_date.strftime("%Y-%m-%d")

    @classmethod
    def get_nearest_expiration_date(cls, products: list[Product]) -> str:
        dates = [
            datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
            for product in products
        ]

        not_expired_dates = [
            date
            for date in dates
            if date > datetime.today()
        ]

        nearest_date = min(not_expired_dates)
        return nearest_date.strftime("%Y-%m-%d")

    @classmethod
    def get_highest_count_co(cls, products: list[Product]) -> str:
        companies = [
            product["nome_da_empresa"]
            for product in products
        ]

        companies_counter = Counter(companies)
        return companies_counter.most_common()[0][0]
