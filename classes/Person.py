from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, id: str, name: str, age: int, phone_number: str):
        self.id = id
        self.age = age
        self.name = name
        self.phone_number = phone_number
