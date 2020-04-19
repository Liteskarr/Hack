from random import choice
from random import randint


class Event:
    def __init__(self):
        self.globalEvents = ['Rain', 'HardPoliceCheck', 'EasySnow', 'StrongWind', 'Sun']

    def result(self):
        resEvent = self.globalEvents()
        if resEvent in 'Rain':
            return {
                'Вы не можете выйти на улицу из-за сильного дождя....Придется сидеть дома..': {
                    'stress': randint(1, 10)}}
        elif resEvent in 'HardPoliceCheck':
            return {'Усиленно потрулирование улиц, если вы выйдете на улицу то, есть шанс, что вас поймают': {
                'stress': randint(10, 40)}}

        elif resEvent in 'EasySnow':
            return {'На улице идет легкий снег, выходить на улицу можно!': {'stress': randint(-50, -10)}}

        elif resEvent in 'StrongWind':
            return {'На улице штормовой ветер, вам нельзя выходить на улицу..': {'stress': randint(1, 32)}}

        else:
            return {'Сегодня прекрасная погода, самое время выйти на улицу!': {'stress': randint(-20, -50)}}

    def getEvent(self):
        return choice(self.globalEvents)
