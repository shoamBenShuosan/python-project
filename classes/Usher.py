from classes.Food import Food
from classes.Home import Home
from classes import Shop
from interface.ILogistics import ILogistics
from classes.Worker import Worker


class Usher(Worker, ILogistics):
    def __init__(self, id: str, name: str, age: int, phone_number: str, number_worker: str, color_vest: str):
        super().__init__(id, name, age, phone_number, number_worker)
        self.color_vest = color_vest

    def add_product_to_shelf(self, shop: Shop):
        from classes.ValidationHelper import ValidationHelper

        type = input("""What department is the product?
    1-Food products.
    2-Household products.""")
        type = ValidationHelper.choice_valid(type, 2)
        if type == 1:
            Food.add(shop)
        if type == 2:
            Home.add(shop)

    def taking_product_off_the_shelf(self, shop):
        from classes.ValidationHelper import ValidationHelper
        from classes.Product import Product

        type = input("""What department is the product?
            1-Food products.
            2-Household products.""")
        type = ValidationHelper.choice_valid(type, 2)

        if type == 1:
            Product.delete(shop, shop.foods,
                           "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\FoodPy.txt")

        if type == 2:
            Product.delete(shop, shop.home_products,
                           "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\HomePy.txt")

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
        number_worker = UiHandler.receiving_input("number worker")
        color_vest = UiHandler.receiving_input("color vest")
        usher = Usher(id, name, age, phone_number.__str__(), number_worker, color_vest)
        shop.persons.append(usher)
        FileHandler.add_obj_to_file(
            id + "," + name + "," + age.__str__() + "," + phone_number.__str__() + "," + number_worker + "," + color_vest,
            "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\UshersPy.txt")
        print("Updated successfully.\n")
        return usher

    def __str__(self):
        return "ID: " + self.id + "." + " name: " + self.name + "." + " age: " + self.age.__str__() + "." +\
            " phone number: " + self.phone_number.__str__() + "." + " number worker: " + self.number_worker +\
            "." + " color vest: " + self.color_vest

