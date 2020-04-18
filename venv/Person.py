import random


class Person:
    def __init__(self):
        pass


class Father(Person):
    def __init__(self):
        self.name =  ''
        self.surname =  ''
        self.age =  random.randint(20, 60)
        self.condition = []
        super().__init__()


class Mom(Person):
    def __init__(self):
        self.name =  ''
        self.surname =  ''
        self.age =  0
        self.age =  random.randint(20, 55)
        self.condition = []
        super().__init__()


class Con(Person):
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.age = 0
        self.condition = []
        super().__init__()


class Daughter(Person):
    def __init__(self):
        self.name = ''
        self.surname = ''
        self.age = 0
        self.condition = []
        super().__init__()

