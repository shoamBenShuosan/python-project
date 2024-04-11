from classes import Shop
from classes.Food import Food
from classes.Home import Home
from classes.Usher import Usher
from interface.ILogistics import ILogistics
from interface.IManager import IManager
from classes.Worker import Worker


class ShiftManager(Worker, ILogistics, IManager):
    def __init__(self, id: str, name: str, age: int, phone_number: str, number_worker: str, experience_years: int ):
        super().__init__(id, name, age, phone_number, number_worker)
        self.experience_years = experience_years
        self.outstanding = False

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
            Product.delete(shop, shop.foods, "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\FoodPy.txt")

        if type == 2:
            Product.delete(shop, shop.home_products, "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\HomePy.txt")

    def add_worker(self, shop: Shop):
        from classes.Cashier import Cashier
        from classes.ValidationHelper import ValidationHelper

        type = input("""Select an employee type:
    1- usher.
    2- cashier.
    """)
        type = ValidationHelper.choice_valid(type, 2)
        if type == 1:
            Usher.add(shop)
        elif type == 2:
            Cashier.add(shop)

    def remove_worker(self, shop: Shop):
        from classes.FileHandler import FileHandler
        from classes.ValidationHelper import ValidationHelper

        type = input("""Select an employee type:
    1- usher.
    2- cashier.
    """)
        type = ValidationHelper.choice_valid(type, 2)
        if type == 1:
            current_worker = shop.delete_worker(shop.ushers)
            FileHandler.delete_worker(
                "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\UshersPy.txt",
                current_worker.name, current_worker.id)
            shop.pop_worker(shop.ushers, current_worker.id)

        elif type == 2:
            current_worker = shop.delete_worker(shop.cashiers)
            FileHandler.delete_worker(
                "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\CashierPy.txt",
                current_worker.name, current_worker.id)
            shop.pop_worker(shop.cashiers, current_worker.id)

    def get_daily_sales_report(self, shop: Shop):

        if not shop.purchases:
            print("The purchases list is empty")
        else:
            for index in shop.purchases:
                print(index)

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
        experience_years = UiHandler.receiving_input("experience years")
        experience_years = ValidationHelper.valid_int(experience_years)
        shift_manager = ShiftManager(id, name, age, phone_number.__str__(), number_worker, experience_years)
        shop.persons.append(shift_manager)
        shop.shift_managers.append(shift_manager)
        FileHandler.add_obj_to_file(
            id + "," + name + "," + age.__str__() + "," + phone_number.__str__() + "," + number_worker + "," +
            experience_years.__str__(),
            "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\ShiftManagerPy.txt")
        print("Updated successfully.\n")
        return shift_manager

    def __str__(self):
        return "ID: " + self.id + ". " + " name: " + self.name + ". " + " age: " + self.age.__str__() + ". " + \
            " phone number: " + self.phone_number.__str__() + ". " + " number worker: " + self.number_worker + ". " + \
            " experience years: " + self.experience_years.__str__()

