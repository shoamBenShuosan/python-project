from classes.Shop import Shop


class ValidationHelper:
    @staticmethod
    def valid_int(user_input):
        valid = False
        while not valid:
            try:
                user_input = int(user_input)
                valid = True
                return user_input
            except ValueError:
                user_input = input("Invalid input. Please enter a valid number. ")

    @staticmethod
    def choice_valid(choice, size: int):
        while True:
            choice = ValidationHelper.valid_int(choice)
            if 1 <= choice <= size:
                return choice
            else:
                choice = input("Invalid input. Please enter a valid number. ")

    @staticmethod
    def valid_id(shop: Shop):
        id = input("Enter ID:")
        valid = False
        while not valid:
            for person in shop.persons:
                if person.id.__eq__(id):
                    id = input("There is a user with the same ID. try again: ")
                    break
            else:
                return id
