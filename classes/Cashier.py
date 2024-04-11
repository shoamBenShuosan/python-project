from classes import Client, Shop
from classes.Worker import Worker


class Cashier(Worker):

    def __init__(self, id: str, name: str, age: int, phone_number: str, number_worker: str, POS_number: int, experience_years: int):
        super().__init__(id, name, age, phone_number, number_worker)
        self.POS_number = POS_number
        self.experience_years = experience_years

    def making_sale(self, client: Client, shop: Shop):
        client.buy_the_products(shop)

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
        POS_number = UiHandler.receiving_input("POS number")
        POS_number = ValidationHelper.valid_int(POS_number)
        experience_years = UiHandler.receiving_input("experience years")
        experience_years = ValidationHelper.valid_int(experience_years)
        cashier = Cashier(id, name, age, phone_number.__str__(), number_worker, POS_number, experience_years)
        shop.persons.append(cashier)
        FileHandler.add_obj_to_file(
            id + "," + name + "," + age.__str__() + "," + phone_number.__str__() + "," + number_worker + "," + POS_number.__str__() + "," + experience_years.__str__(),
            "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\CashierPy.txt")
        print("Updated successfully.\n")
        return cashier

    def __str__(self):
        return "ID: " + self.id + "." + " name: " + self.name + "." + " age: " + self.age.__str__() + "." + " phone number: " + self.phone_number + "." + " number worker: " + self.number_worker + "." + " POS number: " + self.POS_number.__str__() + "." + " experience_years: " + self.experience_years.__str__() +"."

