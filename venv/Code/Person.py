import random


class Person:
    """ Персонаж. """
    STRESS_LIMIT = 100
    HUNGER_LIMIT = 100
    WATER_LIMIT = 100
    HP_LIMIT = 100

    def __init__(self, name: str, surname: str, age: int, special: dict={}, skills: set=set()):
        """ Конструктор. """
        self.name = name
        self.surname = surname
        self.age = age
        self.control = 100
        self.hunger = 100
        self.water = 100
        self.hp = 100
        self.skills = skills
        self.special = special

    def damage(self, mhp):
        self.hp -= mhp
        if self.hp < 0 :
            self.hp = 0

    def eat(self, hunger):
        """ Есть. """
        self.hunger += hunger
        if self.hunger > 100:
            self.hunger == 100

    def left_hunger(self, hunger):
        """ Голодать. """
        self.hunger -= hunger
        if self.hunger < 0:
            self.damage(abs(self.hunger))
            self.hunger = 0

    def drink(self, water):
        self.water += water
        if self.water > self.WATER_LIMIT:
            self.water = self.WATER_LIMIT

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

    def relax(self, stress_point):
        self.control += stress_point
        if self.control > self.STRESS_LIMIT:
            self.control = self.STRESS_LIMIT
