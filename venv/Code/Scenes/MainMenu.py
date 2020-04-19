import threading, time

from Code.Scene import Scene
from Code.RenderObjects.Border import Border
from Code.RenderObjects.Button import Button

import keyboard
from colorama import Back



class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.add_render(Border(Back.CYAN + ' ' + Back.RESET))

    def listen_clicks(self, e: keyboard._keyboard_event):
        pass

    def start(self):
        keyboard.hook(self.listen_clicks)

    def update(self):
        keyboard.wait('up')
        keyboard.wait('down')
        keyboard.wait('left')
        keyboard.wait('right')
        keyboard.wait('enter')