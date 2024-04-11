from classes.Person import Person


class Worker(Person):
    def __init__(self, id: str, name: str, age: int, phone_number: str, number_worker: str):
        super().__init__(id, name, age, phone_number)
        self.number_worker = number_worker

    def __str__(self):
        return "ID: " + self.id + "." + " name: " + self.name + "." + " age: " + self.age.__str__() + "." + " phone number: " + self.phone_number + "." + " number worker: " + self.number_worker

