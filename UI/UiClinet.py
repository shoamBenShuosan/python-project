from classes.ValidationHelper import ValidationHelper
from classes.Client import Client


class UiClinet:

    @staticmethod
    def display_main_menu(client: Client):
        choice = input("welcome " + client.name + """ what would you like to do?
    1- Add a product from the shelf to the cart.
    2- Purchasing the products in my shopping cart.
    3- Log in as another user (go beck).
    """)
        choice = ValidationHelper.choice_valid(choice, 3)
        return choice
