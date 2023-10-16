"""
Шаг 2 - Green.
Давайте напишем класс c добавлением продукта в инвентарь
"""


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_products(self):
        return self.products
    
    """
    Повторите шаг 2 - green.
    Давайте напишем класс c добавлением продукта в инвентарь
    """
    def get_final_price(self):
        sum_price = 0
        for product in self.products:
            sum_price += product.price
        return sum_price


