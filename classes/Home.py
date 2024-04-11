from classes.Product import Product
from classes import Shop


class Home(Product):
    def __init__(self, name: str, code: str, price: float):
        super().__init__(name, code, price)

    @staticmethod
    def add(shop: Shop):
        from classes.FileHandler import FileHandler
        from classes.ValidationHelper import ValidationHelper

        name = input("Enter the name of product: ")
        code = input("Enter the code of product: ")
        price = input("Enter the price of product: ")
        price = ValidationHelper.valid_int(price)
        home_product = Home(name, code, float(price))
        shop.products.append(home_product)
        shop.home_products.append(home_product)
        FileHandler.add_obj_to_file(home_product.str_to_file(),
                                    "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\HomePy.txt")
        print("\nThe product has been successfully added\n ")

    def str_to_file(self):
        return self.name + "," + self.code + "," + self.price.__str__()
