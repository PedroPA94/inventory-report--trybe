from inventory_report.inventory.product import Product


def test_relatorio_produto():
    """Verifica se o relatório de um produto é gerado corretamente"""

    test_product = {
        "id": 1,
        "nome": "Testanol",
        "empresa": "Test Inc.",
        "fabricacao": "01/01/2020",
        "validade": "01/01/2025",
        "numero_de_serie": "SOLONG42",
        "armazenamento": "Mantenha fora do alcance de crianças"
    }

    product = Product(
        test_product["id"],
        test_product["nome"],
        test_product["empresa"],
        test_product["fabricacao"],
        test_product["validade"],
        test_product["numero_de_serie"],
        test_product["armazenamento"],
    )

    expected_report = (
            f"O produto {test_product['nome']}"
            f" fabricado em {test_product['fabricacao']}"
            f" por {test_product['empresa']} com validade"
            f" até {test_product['validade']}"
            f" precisa ser armazenado {test_product['armazenamento']}."
    )

    report = str(product)

    assert expected_report == report
