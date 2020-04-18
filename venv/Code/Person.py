import random


class Person:
    """ Персонажи. """
    LIMIT_CONTROL = 100
    LIMIT_STRESS = 100
    LIMIT_HUNGER = 100
    LIMIT_WATER = 100
    LIMIT_HP = 100
    LIMIT_BUFF = 5
    LIMIT_DE_BUFF = 5

    def __init__(self, name: str, surname: str, age: int, special: dict = {}, skills: set = set(),
                 buff: list = list(), de_buff: list = list()):
        """ Конструктор. """
        self.name, self.surname, self.age = name, surname, age
        self.control,  self.hunger, self.water, self.hp, self.stress = LIMIT_CONTROL, LIMIT_HUNGER, LIMIT_WATER, LIMIT_HP, LIMIT_STRESS
        self.skills, self.special = skills, special
        self.buff, self.de_buff = buff, de_buff

    def damage(self, dmg):
        """ Урон. """
        self.hp -= dmg
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
        """ Пить."""
        self.water += water
        # Лимит.
        self.water = self.WATER_LIMIT if self.water > self.WATER_LIMIT else self.water

    def left_water(self, water):
        """ Жажда. """
        self.water -= water
        if self.water < 0:
            self.damage(2 * abs(self.water))
            self.water = 0

    def get_stress(self, stress_points):
        """ Стресс. """
        self.stress -= stress_points
        if self.control < 0:
            self.damage(int(0.5 * abs(self.stress)))
            self.control = 0

    def relax(self, relax_points):
        """ Отдых. """
        self.control += relax_points
        if self.control > self.STRESS_LIMIT:
            self.control = self.STRESS_LIMIT

    def add_buff(self, buffs):
        """ Добавление бафа. """
        if len(self.buff) < LIMIT_BUFF:
            self.buff.append(buffs)
        else:
            print('Количество бафов максимально')

    def add_de_buff(self, de_buffs):
        """ Добавление дебафа."""
        if len(self.de_buff) < LIMIT_DE_BUFF:
            self.de_buff.append(de_buffs)
        else:
            print('Количество дебафов максимально')
