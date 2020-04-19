import random
import time


RAND_SEED = random.randint(0, 100)
LIMIT_CONTROL, LIMIT_STRESS = 100, 100
LIMIT_HP, LIMIT_HUNGER, LIMIT_WATER = 100, 100, 100
LIMIT_BUFF = 3
LIMIT_DE_BUFF = 3
TIME_SECONDS = 2
SPECIAL_BASE_PRINT = {'Smart': 'Персонаж имеет повышенный уровень интеллекта.',
                      'stupid': 'Персонаж имеет пониженный уровень интеллекта.',
                      'light sleep': 'Персонаж чуток во сне.',
                      'strong': 'Персонаж в хорошей физической форме.',
                      'frail': 'Персонаж в плохой физической форме.',
                      'glutton': 'Персонаж любит покушать.',
                      '': '',
                      '': ''}
PERSON_EVENTS = ['fracture']
PERSON_EVENTS_PRINT = {'fracture': 'Вы всподкнулись и получили перелом.',
                       'overeaten': 'Вы слишком много съели и объелись.',
                       'full_eat': 'Вы вкусно покушали и чувствуете сытость.',
                       '': ''}


class Person:
    """ Персонажи. """

    def __init__(self, name: str = 'Имя', surname: str = 'фамилия', age: int = 0,
                 special: dict = dict(), skills: set = set(), buff: list = set(), de_buff: list = set()):
        """ Конструктор. """
        self.name, self.surname, self.age = name, surname, age
        self.control,  self.hunger, self.water = LIMIT_CONTROL, LIMIT_HUNGER, LIMIT_WATER
        self.hp, self.stress = LIMIT_HP, LIMIT_STRESS
        self.skills, self.special = skills, special
        self.buff, self.de_buff = buff, de_buff
        self.temp = []

    def damage(self, dmg):
        """ Урон. """
        self.hp -= dmg
        # Лимит.
        self.hp = 0 if self.hp < 0 else self.hp

    def eat(self, hunger):
        """ Есть. """
        self.hunger += hunger
        # Лимит.
        if self.hunger > 60 and (self.hunger < 100):
            # сытость
            print(PERSON_EVENTS_PRINT['full_eat'])
            Person.add_buff(self, 'full_eat')
        elif self.hunger > 100:
            # объелся
            print(PERSON_EVENTS_PRINT['overeaten'])
            Person.add_de_buff(self, 'overeaten')
            self.hunger = 100

    def left_hunger(self, hunger):
        """ Голодать. """
        self.hunger -= hunger
        if self.hunger < 0:
            self.damage(abs(self.hunger))
            if Person.is_live(self) is False:
                print(f'Персонаж погиб в результате голода.')
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
            if Person.is_live(self) is False:
                print(f'Персонаж погиб в результате жажды.')
            self.water = 0

    def get_stress(self, stress_points):
        """ Стресс. """
        self.stress -= stress_points
        if self.control < 0:
            self.damage(int(0.5 * abs(self.stress)))
            if Person.is_live(self) is False:
                print(f'Персонаж погиб в результате стресса.')
            self.control = 0

    def relax(self, relax_points):
        """ Отдых. """
        self.control += relax_points
        # Лимит.
        self.control = self.STRESS_LIMIT if self.control > self.STRESS_LIMIT else self.control

    def add_buff(self, buffs):
        """ Добавление бафа. """
        if len(self.buff) < LIMIT_BUFF:
            self.buff.append(buffs)
        else:
            print('Количество бафов максимально')

    def add_de_buff(self, de_buffs):
        """ Добавление дебафа."""
        if len(self.de_buff) < LIMIT_DE_BUFF:
            self.de_buff.add(de_buffs)
            print(f'{PERSON_EVENTS_PRINT[de_buffs]}')
        else:
            print('Количество дебафов максимально')


class Mom(Person):
    def set_name(self):
        self.name = "Имя матери"
        return self.name

    def set_surname(self):
        self.surname = "Фамилия"
        return self.surname

    def set_age(self):
        random.seed(RAND_SEED)
        self.age = random.randint(20, 55)
        return self.age

    def __init__(self):
        self.name, self.surname, self.age = Mom.set_name(self), Mom.set_surname(self), Mom.set_age(self)
        self.ind_mom = []
        super().__init__(self.name, self.surname, self.age)

    def main(self):
        self.ind_mom = [Mom().name, Mom().surname, Mom().age]
        return self.ind_mom


class Dad(Person):
    def set_name(self):
        self.name = "Имя отца"
        return self.name

    def set_surname(self):
        self.surname = "Фамилия"
        return self.surname

    def set_age(self):
        random.seed(RAND_SEED)
        self.age = random.randint(22, 60)
        return self.age

    def __init__(self):
        self.name, self.surname, self.age = Dad.set_name(self), Dad.set_surname(self), Dad.set_age(self)
        self.ind_dad = []
        super().__init__(self.name, self.surname, self.age)

    def main(self):
        self.ind_dad = [Dad().name, Dad().surname, Dad().age]
        return self.ind_dad


class Son(Person):
    def set_name(self):
        self.name = "Имя сына"
        return self.name

    def set_surname(self):
        self.surname = "Фамилия"
        return self.surname

    def set_age(self):
        random.seed(RAND_SEED)
        self.age = random.randint(Son().set_age() - 19, Son().set_age() - 20)
        return self.age

    def __init__(self):
        self.name, self.surname, self.age = Son.set_name(self), Son.set_surname(self), Son.set_age(self)
        self.ind_son = []
        super().__init__(self.name, self.surname, self.age)

    def main(self):
        self.ind_son = [Son().name, Son().surname, Son().age]
        return self.ind_son


class Daughter(Person):
    def set_name(self):
        self.name = "Имя дочери"
        return self.name

    def set_surname(self):
        self.surname = "Фамилия"
        return self.surname

    def set_age(self):
        random.seed(RAND_SEED)
        self.age = random.randint(Mom_Gen().set_age() - 19, Dad_Gen().set_age() - 20)
        return self.age

    def __init__(self):
        self.name, self.surname, self.age = Daughter.set_name(self), Daughter.set_surname(self), Daughter.set_age(self)
        self.ind_dau = []
        super().__init__(self.name, self.surname, self.age)

    def main(self):
        self.ind_dau = [Daughter().name, Daughter().surname, Daughter().age]
        return self.ind_dau


def events_time():
    """Проходит день."""
    for i in range(1, 13):
        if random.randint(1, 4) == 3:
            event = random.choice(PERSON_EVENTS)
            print(f'Сейчас {i} час. Выпало {event}')
            # дебаф добовляем персанажу Mom
            print(Person(*Mom().main()).add_de_buff(event))
        time.sleep(TIME_SECONDS)


def test():
    mam = Mom()
    mam.left_hunger(60)
    print(mam.hunger)
    mam.left_hunger(20)
    print(mam.hunger)


if __name__ == '__main__':
    test()


