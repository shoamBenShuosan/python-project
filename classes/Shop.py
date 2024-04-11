import sys
from typing import List

from classes import Client
from classes.Cashier import Cashier
from classes.Food import Food
from classes.Home import Home
from classes.Person import Person
from classes.Product import Product
from classes import ShiftManager
from classes.Usher import Usher
from classes.Worker import Worker


class Shop:

    __ushers: List[Usher]
    __shift_managers: List['ShiftManager']
    __cashier: List[Cashier]
    __workers: List[Worker]
    __clients: List['Client']
    __persons: List[Person]
    __foods: List[Food]
    __home_products: List[Home]
    __products: List[Product]
    __purchases: []
    __daily_income: float

    def __init__(self):
        from classes.FileHandler import FileHandler

        self.shift_managers = FileHandler.read_shift_manager_file()
        self.cashiers = FileHandler.read_cashier_file()
        administrators = FileHandler.read_administrator_file()
        self.ushers = FileHandler.read_usher_file()
        self.workers = []
        self.workers.extend(self.shift_managers)
        self.workers.extend(self.cashiers)
        self.workers.extend(administrators)
        self.workers.extend(self.ushers)
        self.clients = []
        self.clients = FileHandler.read_client_file()
        self.persons = []
        self.persons.extend(self.workers)
        self.persons.extend(self.clients)
        self.foods = FileHandler.read_food_file()
        self.home_products = FileHandler.read_home_file()
        self.products = []
        self.products.extend(self.foods)
        self.products.extend(self.home_products)
        self.purchases = []
        self.daily_income = 0

    def valid_user(self, user_id: str):
        for person in self.persons:
            if person.id.__eq__(user_id):
                return person
        print("The user is not registered in the system.\n")
        return None

    def register(self):
        from classes.Client import Client
        from classes.ValidationHelper import ValidationHelper
        from classes.Administrator import Administrator
        from classes.ShiftManager import ShiftManager

        type = input("""Welcome to registration!
        
    Select your user type:
    1- client.
    2- usher.
    3- cashier.
    4- shift manager.
    5- administrator .
    6- go back to log in.
    """)
        type = ValidationHelper.choice_valid(type, 6)
        if type == 1:
            return Client.add(self)

        elif type == 2:
            return Usher.add(self)

        elif type == 3:
            return Cashier.add(self)

        elif type == 4:
            return ShiftManager.add(self)

        elif type == 5:
            return Administrator.add(self)

        elif type == 6:
            return self.login()

    def login(self):
        from classes.ValidationHelper import ValidationHelper

        user_id = input("""Welcome!
Enter your ID:
(press 0 to log out)
""")
        user_id = ValidationHelper.valid_int(user_id)
        if user_id == 0:
            sys.exit(0)
        current_user = self.valid_user(user_id.__str__())
        if current_user is None:
            person = self.register()
        else:
            person = current_user
        return person

    def find_cashier(self, client: Client):
        cashier = None
        for worker in self.workers:
            if isinstance(worker, Cashier):
                cashier = worker
                break
        print(
            "Hello " + client.name + " My name is " + cashier.name + " and I am your cashier\nwelcome to POS "
            + cashier.POS_number.__str__())
        return cashier

    def delete_worker(self, workers: [Worker]):
        from classes.ValidationHelper import ValidationHelper

        index = 1
        for worker in workers:
            print(index.__str__() + "." + worker.__str__() + "\n")
            index += 1
        current_worker = input("Select the number of worker you want to remove from shelf.")
        current_worker = ValidationHelper.choice_valid(current_worker, len(workers))

        i = 0
        for person in self.persons:
            if person.id == workers[current_worker - 1].id:
                self.persons.pop(i)
                break
            i += 1

        return workers[current_worker - 1]

    def pop_worker(self, workers: [Worker], id):
        i = 0
        for worker in workers:
            if worker.id == id:
                workers.pop(i)
            i += 1
        print("Updated successfully.\n")

    @staticmethod
    def open_day():
        from UI.UiClinet import UiClinet
        from UI.UiUsher import UiUsher
        from UI.UiShiftManager import UiShiftManager
        from classes.Administrator import Administrator
        from UI.UiAdministrator import UiAdministrator
        from classes.Client import Client
        from classes.ShiftManager import ShiftManager

        shop = Shop()
        person = shop.login()

        while True:
            if isinstance(person, Client):
                choice = UiClinet.display_main_menu(person)
                if choice == 1:
                    person.add_product_to_cart(shop.products)
                elif choice == 2:
                    cashier = shop.find_cashier(person)
                    cashier.making_sale(person, shop)
                elif choice == 3:
                    person = shop.login()

            if isinstance(person, Usher):
                choice = UiUsher.display_main_menu(person)
                if choice == 1:
                    person.add_product_to_shelf(shop)
                elif choice == 2:
                    person.taking_product_off_the_shelf(shop)
                elif choice == 3:
                    person = shop.login()

            if isinstance(person, ShiftManager):
                choice = UiShiftManager.display_main_menu(person)
                if choice == 1:
                    person.add_product_to_shelf(shop)
                elif choice == 2:
                    person.taking_product_off_the_shelf(shop)
                elif choice == 3:
                    person.add_worker(shop)
                elif choice == 4:
                    person.remove_worker(shop)
                elif choice == 5:
                    person.get_daily_sales_report(shop)
                elif choice == 6:
                    person = shop.login()

            if isinstance(person, Administrator):
                choice = UiAdministrator.display_main_menu(person)
                if choice == 1:
                    person.display_product_list(shop)
                elif choice == 2:
                    person.add_worker(shop)
                elif choice == 3:
                    person.remove_worker(shop)
                elif choice == 4:
                    person.get_daily_sales_report(shop)
                elif choice == 5:
                    person = shop.login()

            if isinstance(person, Cashier):
                person = shop.login()
