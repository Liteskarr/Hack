from random import choice


class Event:
    def __init__(self):
        self.globalEvents = ['Rain', 'HardPoliceCheck', 'EasySnow', 'StrongWind', 'Sun']

    def result(self):
        resEvent = self.globalEvents()
        if resEvent in 'Rain':
            return 'Вы не можете выйти на улицу из-за сильного дождя....' \
                   'Придется сидеть дома..'
        elif resEvent in 'HardPoliceCheck':
            return 'Усиленно потрулирование улиц, если вы выйдете на улицу то, есть шанс, что вас поймают'

        elif resEvent in 'EasySnow':
            return 'На улице идет легкий снег, выходить на улицу можно!'

        elif resEvent in 'StrongWind':
            return 'На улице штормовой ветер, вам нельзя выходить на улицу..'

        else:
            return 'Сегодня прекрасная погода, самое время выйти на улицу!'

    def getEvent(self):
        return choice(self.globalEvents)
