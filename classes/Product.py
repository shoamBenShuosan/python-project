from abc import ABC
from typing import List

from classes import Shop


class Product(ABC):
    def __init__(self, name: str, code: str, price: float):
        self.name = name
        self.code = code
        self.price = price

    def __str__(self):
        return "name: " + self.name + "." + " code: " + self.code + "." + " price: " + self.price.__str__()

    @staticmethod
    def delete(shop: Shop, current_products: List, file_path: str):
        from classes.FileHandler import FileHandler
        from classes.ValidationHelper import ValidationHelper

        index = 1
        for product in current_products:
            print(index.__str__() + "." + product.__str__() + "\n")
            index += 1
        current_product = input("Select the number of product you want to remove from shelf.")
        current_product = ValidationHelper.choice_valid(current_product, len(current_products))
        FileHandler.delete_product_from_file(current_products[current_product - 1].code, file_path)
        shop.products.pop(current_product - 1)
        current_products.pop(current_product - 1)
        print("the transaction completed successfully\n")

    @staticmethod
    def add(shop: Shop):
        pass

    def str_to_file(self):
        return self.name + "," + self.code + "," + self.price.__str__()
