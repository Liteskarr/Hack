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

    def __init__(self, name: str = 'Имя', surname: str = 'фамилия', age: int = 35,
                 hp: int = LIMIT_HP, stress: int = LIMIT_STRESS, control: int = LIMIT_CONTROL,
                 hunger: int = LIMIT_HUNGER, water: int = LIMIT_WATER,
                 special: dict = dict(), skills: set = set(), buff: list = set(), de_buff: list = set()):
        """ Конструктор. """
        self.name, self.surname, self.age = name, surname, age
        self.control,  self.hunger, self.water = control, hunger, water
        self.hp, self.stress = hp, stress
        self.skills, self.special = skills, special
        self.buff, self.de_buff = buff, de_buff

    def v_vid(self):
        self.temp = [self.name, self.surname, self.age, self.hp, self.stress, self.control,
                     self.hunger, self.water, self.special, self.skills, self.buff, self.de_buff]
        return self.temp

    def is_live(self):
        if self.hp == 0:
            return False
        return True

    def damage(self, dmg):
        """ Урон. """
        # Жив ли?
        if Person.is_live(self) is False:
            print(f'Персонаж мёртв')
        else:
            self.hp -= dmg
            # Лимит.
            self.hp = 0 if self.hp < 0 else self.hp
        return Person.v_vid(self)

    def eat(self, hunger):
        """ Есть. """
        # Жив ли?
        if Person.is_live(self) is False:
            print(f'Персонаж мёртв.')
        else:
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
        return Person.v_vid(self)

    def left_hunger(self, hunger):
        """ Голодать. """
        # Жив ли?
        if Person.is_live(self) is False:
            print(f'Персонаж мёртв.')
        else:
            self.hunger -= hunger
            if self.hunger < 0:
                self.damage(abs(self.hunger))
                if Person.is_live(self) is False:
                    print(f'Персонаж погиб в результате голода.')
                self.hunger = 0

    def drink(self, water):
        """ Пить."""
        # Жив ли?
        if Person.is_live(self) is False:
            print(f'Персонаж мёртв.')
        else:
            self.water += water
            # Лимит.
            self.water = self.WATER_LIMIT if self.water > self.WATER_LIMIT else self.water
        return Person.v_vid(self)

    def left_water(self, water):
        """ Жажда. """
        # Жив ли?
        if Person.is_live(self) is False:
            print(f'Персонаж мёртв.')
        else:
            self.water -= water
            if self.water < 0:
                self.damage(2 * abs(self.water))
                if Person.is_live(self) is False:
                    print(f'Персонаж погиб в результате жажды.')
                self.water = 0
        return Person.v_vid(self)

    def get_stress(self, stress_points):
        """ Стресс. """
        # Жив ли?
        if Person.is_live(self) is False:
            print(f'Персонаж мёртв.')
        else:
            self.stress -= stress_points
            if self.control < 0:
                self.damage(int(0.5 * abs(self.stress)))
                if Person.is_live(self) is False:
                    print(f'Персонаж погиб в результате стресса.')
                self.control = 0
        return Person.v_vid(self)

    def relax(self, relax_points):
        """ Отдых. """
        # Жив ли?
        if Person.is_live(self) is False:
            print(f'Персонаж мёртв')
        else:
            self.control += relax_points
            # Лимит.
            self.control = self.STRESS_LIMIT if self.control > self.STRESS_LIMIT else self.control
        return Person.v_vid(self)

    def add_buff(self, buffs):
        """ Добавление бафа. """
        # Жив ли?
        if Person.is_live(self) is False:
            print(f'Персонаж мёртв')
        else:
            if len(self.buff) < LIMIT_BUFF:
                self.buff.append(buffs)
            else:
                print('Количество бафов максимально')
        return Person.v_vid(self)

    def add_de_buff(self, de_buffs):
        """ Добавление дебафа."""
        # Жив ли?
        if Person.is_live(self) is False:
            print(f'Персонаж мёртв')
        else:
            if len(self.de_buff) < LIMIT_DE_BUFF:
                self.de_buff.add(de_buffs)
                print(self.de_buff)
                print(f'{PERSON_EVENTS_PRINT[de_buffs]}')
            else:
                print('Количество дебафов максимально')
        return Person.v_vid(self)


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
    mom = Person(name='Mama')
    dad = Person(name='Dad')
    mom.left_hunger(6)
    print(mom.hunger)
    mom.left_hunger(6)
    print(mom.hunger)


if __name__ == '__main__':
    test()
