from classes.FileHandler import FileHandler
from classes.ShiftManager import ShiftManager
from classes.Shop import Shop
from classes.Usher import Usher
from interface.IManager import IManager
from classes.Worker import Worker


class Administrator(Worker, IManager):
    def __init__(self, id: str, name: str, age: int, phone_number: str, number_worker: str, experience_years: int):
        super().__init__(id, name, age, phone_number, number_worker)
        self.experience_years = experience_years
        self.outstanding = False

    def display_product_list(self, shop: Shop):
        for product in shop.products:
            print(product.__str__())

    def add_worker(self, shop: Shop):
        from classes.Cashier import Cashier
        from classes.ValidationHelper import ValidationHelper

        type = input("""Select an employee type:
    1- usher.
    2- cashier.
    3- shift manager.
    """)
        type = ValidationHelper.choice_valid(type, 3)
        if type == 1:
            Usher.add(shop)
        elif type == 2:
            Cashier.add(shop)
        elif type == 3:
           ShiftManager.add(shop)

    def remove_worker(self, shop: Shop):
        from classes.ValidationHelper import ValidationHelper

        type = input("""Select an employee type:
    1- usher.
    2- cashier.
    3- shift manager.
    """)
        type = ValidationHelper.choice_valid(type, 3)
        if type == 1:
            current_worker = shop.delete_worker(shop.ushers)
            FileHandler.delete_worker(
                "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\UshersPy.txt",
                current_worker.name, current_worker.id)
            shop.pop_worker(shop.ushers, current_worker.id)

        elif type == 2:
            from classes.Cashier import Cashier
            current_worker = shop.delete_worker(shop.cashiers)
            FileHandler.delete_worker(
                "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\CashierPy.txt",
                current_worker.name, current_worker.id)
            shop.pop_worker(shop.cashiers, current_worker.id)

        elif type == 3:
            current_worker = shop.delete_worker(shop.shift_managers)
            FileHandler.delete_worker(
                "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\ShiftManagerPy.txt",
                current_worker.name, current_worker.id)
            shop.pop_worker(shop.shift_managers, current_worker.id)

    def get_daily_sales_report(self, shop: Shop):

        if not shop.purchases:
            print("The purchases list is empty")
        else:
            for index in shop.purchases:
                print(index)

        print("Total revenue today: " + shop.daily_income.__str__())

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
        adminstrator = Administrator(id, name, age, phone_number, number_worker, experience_years)
        shop.persons.append(adminstrator)
        FileHandler.add_obj_to_file(
            id + "," + name + "," + age.__str__() + "," + phone_number.__str__() + "," + number_worker + "," +
            experience_years.__str__(), "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\AdministratorPy.txt")
        return adminstrator
