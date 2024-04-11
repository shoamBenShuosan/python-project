from classes.ShiftManager import ShiftManager
from classes.ValidationHelper import ValidationHelper


class UiShiftManager:

    @staticmethod
    def display_main_menu(shift_manager: ShiftManager):
        choice = input("welcome " + shift_manager.name + """ what would you like to do?
    1- Add a product to the shelf.
    2- Remove a product from the shelf.
    3- Add worker.
    4- Remove worker. 
    5- View daily sales report.
    6- Log in as another user (go beck).
    """)
        choice = ValidationHelper.choice_valid(choice, 6)
        return choice
