import random
import time


RAND_SEED = random.randint(0, 100)
LIMIT_CONTROL = 100
LIMIT_STRESS = 100
LIMIT_HUNGER = 100
LIMIT_WATER = 100
LIMIT_HP = 100
LIMIT_BUFF = 5
LIMIT_DE_BUFF = 5
TIME_SECONDS = 2
PERSON_EVENTS = ['fracture', 'overeaten']
PERSON_EVENTS_PRINT = {'fracture': 'Вы всподкнулись и получили перелом.',
                       'overeaten': 'Вы слишком много съели и объелись.',
                       'full_eat': 'Вы вкусно покушали и чувствуете сытость.',
                       '': ''}


class Person:
    """ Персонажи. """

    def __init__(self, name: str, surname: str, age: int, special: dict = dict(), skills: set = set(),
                 hp: int = LIMIT_HP, control: int = LIMIT_CONTROL, hunger: int = LIMIT_HUNGER,
                 water: int = LIMIT_WATER, buff: list = set(), de_buff: list = set()):
        """ Конструктор. """
        self.name, self.surname, self.age = name, surname, age
        self.control,  self.hunger, self.water = control, hunger, water
        self.hp, self.stress = hp, stress
        self.skills, self.special = skills, special
        self.buff, self.de_buff = buff, de_buff

    def damage(self, dmg):
        """ Урон. """
        self.hp -= dmg
        # Лимит.
        self.hp = 0 if self.hp < 0 else self.hp
        if self.hp == 0:
            print(f'Персонаж умер.')

    def eat(self, hunger):
        """ Есть. """
        self.hunger += hunger
        # Лимит.
        if self.hunger > 60 and (self.hunger < 100):
            # сытость
            print(PERSON_EVENTS_PRINT['full_eat'])
            add_buff(self, 'full_eat')
        elif self.hunger > 100:
            # объелся
            print(PERSON_EVENTS_PRINT['overeaten'])
            add_de_buff(self, 'overeaten')
            self.hunger = 100

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
            print(self.de_buff)
            print(f'{PERSON_EVENTS_PRINT[de_buffs]}')
        else:
            print('Количество дебафов максимально')

    def main(self):
        return self.name, self.age


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

    def set_special(self):
        self.special = {}
        return self.special

    def set_skills(self):
        self.skills = set()
        return self.skills

    def __init__(self):
        self.control, self.hunger, self.water = LIMIT_CONTROL, LIMIT_HUNGER, LIMIT_WATER
        self.hp, self.stress = LIMIT_HP, LIMIT_STRESS

        self.name, self.surname = Mom.set_name(self), Mom.set_surname(self)
        self.special, self.age, self.skills = Mom.set_special(self),  Mom.set_age(self), Mom.set_skills(self)
        self.ind_mom = []
        super().__init__(self.name, self.surname, self.age, self.special,
                         self.skills, self.hp, self.control, self.hunger, self.water)

    def main(self):
        self.ind_mom = [Mom().name, Mom().surname, Mom().age, Mom().special, Mom().skills,
                        Mom().hp, Mom().stress, Mom().control, Mom().hunger, Mom().water]
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

    def set_special(self):
        self.special = {}
        return self.special

    def set_skills(self):
        self.skills = set()
        return self.skills

    def __init__(self):
        self.name, self.surname = Dad.set_name(self), Dad.set_surname(self)
        self.special, self.age, self.skills = Dad.set_special(self), Dad.set_age(self), Dad.set_skills(self)
        self.ind_dad = []
        super().__init__(self.name, self.surname, self.age, self.special, self.skills)

    def main(self):
        self.ind_dad = [Dad().name, Dad().surname, Dad().age, Dad().special, Dad().skills]
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
        self.age = random.randint(Mom().set_age() - 19, Dad().set_age() - 20)
        return self.age

    def set_special(self):
        self.special = {}
        return self.special

    def set_skills(self):
        self.skills = set()
        return self.skills

    def __init__(self):
        self.name, self.surname = Son.set_name(self), Son.set_surname(self)
        self.special, self.age, self.skills = Son.set_special(self), Son.set_age(self), Son.set_skills(self)
        self.ind_son = []
        super().__init__(self.name, self.surname, self.age, self.special, self.skills)

    def main(self):
        self.ind_son = [Son().name, Son().surname, Son().age, Son().special, Son().skills]
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
        self.age = random.randint(Mom().set_age() - 19, Dad().set_age() - 20)
        return self.age

    def set_special(self):
        self.special = {}
        return self.special

    def set_skills(self):
        self.skills = set()
        return self.skills

    def __init__(self):
        self.name, self.surname, self.age = Daughter.set_name(self), Daughter.set_surname(self), Daughter.set_age(self)
        self.special, self.skills = Daughter.set_special(self), Daughter.set_skills(self)
        self.ind_daughter = []
        super().__init__(self.name, self.surname, self.age, self.special, self.skills)

    def main(self):
        self.ind_daughter = [Daughter().name, Daughter().surname, Daughter().age, Daughter().special, Daughter().skills]
        return self.ind_daughter


def events_time():
    """Проходит день."""
    for i in range(1, 13):
        if random.randint(1, 6) == 3:
            event = random.choice(PERSON_EVENTS)
            print(f'Сейчас {i} час. Выпало {event}')
            # дебаф добовляем персанажу Mom
            print(Person(*Mom().main()).add_de_buff(event))
        time.sleep(TIME_SECONDS)


def test():
    print(Mom().main())

    print(Person(*Mom().main()).main())
    print('     ')
    print(Dad().main())
    print(Person(*Dad().main()).main())
    print('     ')
    print(Son().main())
    print(Person(*Son().main()).main())
    print('     ')
    print(Daughter().main())
    print(Person(*Daughter().main()).main())


if __name__ == '__main__':
    test()
