import os
import Code.Canvas as Canvas
import Code.RenderObjects.Border as Border
import Code.RenderObjects.Button as Button
import colorama
from colorama import Back
colorama.init()


def default_update():
    os.system("mode con cols=100 lines=49")

default_update()

can = Canvas.Canvas(10, 10)

b = Button.Button(1, 1)

can.draw()

input()