import os
import Canvas as Canvas


def default_update():
    os.system("mode con cols=100 lines=49")

default_update()

can = Canvas.Canvas(size_y=49)

input()