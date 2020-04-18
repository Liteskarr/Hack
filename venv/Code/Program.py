import os
import Code.Canvas as Canvas
import Code.RenderObjects.Border as Border
import colorama
from colorama import Back
colorama.init()


def default_update():
    os.system("mode con cols=100 lines=49")

default_update()

can = Canvas.Canvas(40, 40)

can.draw()

input()
input()