import os

from classes.Client import Client
from classes.Food import Food
from classes.Home import Home
from classes.Product import Product
from classes.Usher import Usher
from classes.Cashier import Cashier


class FileHandler:

    @staticmethod
    def read_shift_manager_file():
        from classes.ShiftManager import ShiftManager

        file_path = "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\ShiftManagerPy.txt"
        shift_managers = []

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(',')
                    if len(data) == 6:
                        shift_manager = ShiftManager(*data)
                        shift_managers.append(shift_manager)
        return shift_managers

    @staticmethod
    def read_cashier_file():
        file_path = "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\CashierPy.txt"
        cashiers = []

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(',')
                    if len(data) == 7:
                        cashier = Cashier(*data)
                        cashiers.append(cashier)
        return cashiers

    @staticmethod
    def read_administrator_file():
        from classes.Administrator import Administrator

        file_path = "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\AdministratorPy.txt"
        administrators = []

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(',')
                    if len(data) == 6:
                        administrator = Administrator(*data)
                        administrators.append(administrator)
        return administrators

    @staticmethod
    def read_usher_file():
        file_path = "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\UshersPy.txt"
        ushers = []

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(',')
                    if len(data) == 6:
                        usher = Usher(*data)
                        ushers.append(usher)
        return ushers

    @staticmethod
    def read_client_file():
        from classes.Client import Client

        file_path = "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\ClientPy.txt"
        clients = []

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(',')
                    if len(data) == 4:
                        client = Client(*data)
                        clients.append(client)
        return clients

    @staticmethod
    def read_food_file():
        file_path = "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\FoodPy.txt"
        foods = []

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(',')
                    if len(data) == 3:
                        food = Food(*data)
                        foods.append(food)
        return foods

    @staticmethod
    def read_home_file():
        file_path = "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\HomePy.txt"
        homes = []

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(',')
                    if len(data) == 3:
                        home = Home(*data)
                        homes.append(home)
        return homes

    @staticmethod
    def read_purchases_file(client: Client):
        file_path = "C:\\Users\\ADMIN\\Desktop\\שהם\\פרוייקט פייתון סמסטר ב\\python fail\\purchasesPy.txt"
        purchases = []

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(',')
                    if data[0] == client.name and len(data) == 4:
                        purchase = Product(data[1], data[2], float(data[3]))
                        purchases.append(purchase)
        return purchases

    @staticmethod
    def add_obj_to_file(line, filename):
        with open(filename, 'a') as file:
            file.write(line + '\n')

    @staticmethod
    def delete_product_from_file(code: str, file_path):
        # יוצר קובץ חדש ומעביר אליו שורה אחרי שורה חוץ מהשורה שבה מופיע הקוד של המוצר שרוצים למחוק, לבסוף משנה את הדם הקובץ לקובץ הראשון שהיה.

        temp_file_path = file_path + ".tmp"

        try:
            with open(file_path, "r") as input_file, open(temp_file_path, "w") as temp_file:
                for line in input_file:
                    line = line.strip()
                    if line:
                        parts = line.split(",")
                        if len(parts) == 3 and parts[1] != code:
                            temp_file.write(line + "\n")

            os.replace(temp_file_path, file_path)
            print("Updated successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:", str(e))

    @staticmethod
    def delete_worker(file_path, name, id):
        # קורא את כל השורות ומכניס לרשימה, מחפש את השורה שבה מופיע השם והמספר זהות מוחק אותה, וכותב את הכל בקובץ מחדש
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if name in line and id in line:
                del lines[i]
                break
        else:
            print(f"No line with '{name}'='{id}' found.")
            return

        with open(file_path, 'w') as file:
            file.writelines(lines)

        print("deleted successfully.")

