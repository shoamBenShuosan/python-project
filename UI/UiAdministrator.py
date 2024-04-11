from classes.Administrator import Administrator
from classes.ValidationHelper import ValidationHelper


class UiAdministrator:

    @staticmethod
    def display_main_menu(admin: Administrator):
        choice = input("welcome " + admin.name + """ what would you like to do?
    1- View the list of products in the market.
    2- Add worker.
    3- Remove worker.
    4- View daily sales report. 
    5- Log in as another user (go beck).
    """)
        choice = ValidationHelper.choice_valid(choice, 5)
        return choice



