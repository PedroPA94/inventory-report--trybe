from inventory_report.inventory.product import Product


def test_cria_produto():
    """Verifica se o produto é inicializado com os parâmetros corretos"""

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

    assert product.id == test_product["id"]
    assert product.nome_do_produto == test_product["nome"]
    assert product.nome_da_empresa == test_product["empresa"]
    assert product.data_de_fabricacao == test_product["fabricacao"]
    assert product.data_de_validade == test_product["validade"]
    assert product.numero_de_serie == test_product["numero_de_serie"]
    assert product.instrucoes_de_armazenamento == test_product["armazenamento"]
