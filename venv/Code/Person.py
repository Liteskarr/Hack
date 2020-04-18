import random


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Father(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)


class Mom(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)


class Son(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)


class Daughter(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
