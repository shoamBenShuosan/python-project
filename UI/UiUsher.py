from classes.Usher import Usher
from classes.ValidationHelper import ValidationHelper


class UiUsher:

    @staticmethod
    def display_main_menu(usher: Usher):
        choice = input("welcome " + usher.name + """ what would you like to do?
        1- Add a product to the shelf.
        2- Remove a product from the shelf.
        3- Log in as another user (go beck).
        """)
        choice = ValidationHelper.choice_valid(choice, 3)
        return choice