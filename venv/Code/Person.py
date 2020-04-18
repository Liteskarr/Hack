import random


class Person:
    """ Персонаж. """
    CONTROL_LIMIT = 100
    STRESS_LIMIT = 100
    HUNGER_LIMIT = 100
    WATER_LIMIT = 100
    HP_LIMIT = 100

    def __init__(self, name: str, surname: str, age: int, special: dict = {}, skills: set = set()):
        """ Конструктор. """
        self.name, self.surname, self.age = name, surname, age
        self.control,  self.hunger, self.water, self.hp = CONTROL_LIMIT, HUNGER_LIMIT, WATER_LIMIT, HP_LIMIT
        self.skills = skills
        self.special = special

    def damage(self, mhp):
        self.hp -= mhp
        # Лимит.
        self.hp = 0 if self.hp < 0 else self.hp

    def eat(self, hunger):
        """ Есть. """
        self.hunger += hunger
        # Лимит.
        self.hunger = 100 if self.hunger > 100 else self.hunger

    def left_hunger(self, hunger):
        """ Голодать. """
        self.hunger -= hunger
        if self.hunger < 0:
            self.damage(abs(self.hunger))
            self.hunger = 0

    def drink(self, water):
        self.water += water
        # Лимит.
        self.water = self.WATER_LIMIT if self.water > self.WATER_LIMIT else self.water

    def left_water(self, water):
        self.water -= water
        if self.water < 0:
            self.damage(2 * abs(self.water))
            self.water = 0

    def get_stress(self, stress_points):
        self.stress -= stress_points
        if self.control < 0:
            self.damage(int(0.5 * abs(self.stress)))
            self.control = 0

    def relax(self, relax_points):
        self.control += relax_points
        if self.control > self.STRESS_LIMIT:
            self.control = self.STRESS_LIMIT
