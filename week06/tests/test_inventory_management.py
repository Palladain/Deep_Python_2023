import time
import pytest

from week06.code.inventory_management import Inventory, Product


"""
Шаг 1 - Red.
Давайте напишем тест для функциональности добавления нового товара. 
"""

def test_add_product_to_inventory():
    # your code:
    inventory = Inventory()
    product = Product(name="Новый товар", price=50.0, quantity=10)
    inventory.add_product(product)
    assert product in inventory.get_products()


"""
Давайте повторим шаг 1.

Напишите тест для проверки фунакциональности итоговой суммы всех товаров в инвентаре

"""

def test_final_price():
    # your code:
    inventory = Inventory()
    for price in [10, 20, 30, 40, 50]:
        product = Product(name="Новый товар", price=price, quantity=10)
        inventory.add_product(product)

    assert inventory.get_final_price() == 150
