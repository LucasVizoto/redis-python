from src.models.sqlite.settings.connection import SQLiteConnectionHandler
from .products_repository import ProductsRepository

import pytest

conn_handle = SQLiteConnectionHandler()
conn = conn_handle.connect()
repo = ProductsRepository(conn)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_insert():
    name = 'Test Product'
    price = 18.05
    quantity = 3

    repo.insert_product(name, price, quantity)


@pytest.mark.skip(reason="Interação com o banco de dados")
def test_find_product_by_name():
    name = 'Test Product'
    product = repo.find_product_by_name(name)

    print(product)
    print(type(product))

    assert product is not None
    assert product[1] == name