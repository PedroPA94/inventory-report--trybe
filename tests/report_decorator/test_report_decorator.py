from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    products = [
        {
            "id": 1,
            "nome_do_produto": "Cafe",
            "nome_da_empresa": "Cafes Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "instrucao"
        },
        {
            "id": 2,
            "nome_do_produto": "Cafe2",
            "nome_da_empresa": "Cafes Nature",
            "data_de_fabricacao": "2010-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "instrucao"
        },
        {
            "id": 1,
            "nome_do_produto": "Cafe3",
            "nome_da_empresa": "Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2025-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "instrucao"
        }
    ]

    green_code = '[32m'
    blue_code = '[36m'
    red_code = '[31m'

    report = ColoredReport(SimpleReport).generate(products)

    green_phrases = [
        'Data de fabricação mais antiga',
        'Data de validade mais próxima',
        'Empresa com mais produtos'
    ]

    for phrase in green_phrases:
        phrase_start = report.find(phrase)
        phrase_color_code = report[phrase_start - len(green_code):phrase_start]
        assert phrase_color_code == green_code

    blue_dates = ["2010-07-04", "2025-02-09"]

    for date in blue_dates:
        date_start = report.find(date)
        date_color_code = report[date_start - len(blue_code):date_start]
        assert date_color_code == blue_code

    red_text = "Cafes Nature"

    text_start = report.find(red_text)
    text_color_code = report[text_start - len(red_code):text_start]

    assert text_color_code == red_code
