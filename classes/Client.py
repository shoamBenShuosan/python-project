from typing import List

from classes import Shop
from classes.Person import Person
from classes.Product import Product


class Client(Person):
    __shopping_cart: List[Product]
    __purchases: List[Product]

    def __init__(self, id: str, name: str, age: int, phone_number: str):
        super().__init__(id, name, age, phone_number)
        from classes.FileHandler import FileHandler

        self.shopping_cart = []
        self.purchases = []
        self.purchases = FileHandler.read_purchases_file(self)

    def add_product_to_cart(self, prodacts: List[Product]):
        from classes.ValidationHelper import ValidationHelper

        index = 1
        for prodact in prodacts:
            print(index.__str__() + "." + prodact.__str__() + "\n")
            index += 1
        current_product = input("Select the number of product you wish to add to the cart.")
        current_product = ValidationHelper.choice_valid(current_product, len(prodacts))
        self.shopping_cart.append(prodacts[current_product-1])

        print("your shopping cart :\n")
        for i, product in enumerate(self.shopping_cart):
            print(f"{i + 1}. {product}")
        print("The operation was carried out successfully\n")

    def buy_the_products(self, shop: Shop):
        from classes.FileHandler import FileHandler

        if len(self.shopping_cart) == 0:
            print("Your cart is empty")
        else:
            total_price = 0
            print("your shopping cart:")
            for product in self.shopping_cart:
                print(product.__str__())
                total_price += float(product.price)
                self.purchases.append(product.__str__())
                shop.purchases.append("client name: " + self.name + " " + product.__str__())
                FileHandler.add_obj_to_file(self.name + "," + product.str_to_file(), "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\purchasesPy.txt")
            shop.daily_income += total_price
            self.shopping_cart = []
            print("Your purchase amount is: " + total_price.__str__() + " Thank you for shopping with us.\n")

    @staticmethod
    def add(shop: Shop):
        from classes.ValidationHelper import ValidationHelper
        from classes.FileHandler import FileHandler
        from UI.UiHandler import UiHandler

        id = ValidationHelper.valid_id(shop)
        name = UiHandler.receiving_input("name")
        age = UiHandler.receiving_input("age")
        age = ValidationHelper.valid_int(age)
        phone_number = UiHandler.receiving_input("phone number")
        phone_number = ValidationHelper.valid_int(phone_number)

        client = Client(id, name, age, phone_number.__str__())
        shop.persons.append(client)
        FileHandler.add_obj_to_file(id + "," + name + "," + age.__str__() + "," + phone_number.__str__(),
                                    "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\ClientPy.txt")
        return client
