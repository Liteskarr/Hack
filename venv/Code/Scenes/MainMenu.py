import threading, time

from Code.Scene import Scene
from Code.RenderObjects.Border import Border
from Code.RenderObjects.Button import Button

from pynput import keyboard
from colorama import Back



class MainMenu(Scene):
    def on_release(self, key):
        if key == keyboard.Key.up:
            self.ui_pointer = self.ui_pointer[0], (self.ui_pointer[1] - 1) % len(self.ui_map)
            print('a')
        elif key == keyboard.Key.down:
            self.ui_pointer = self.ui_pointer[0], (self.ui_pointer[1] + 1) % len(self.ui_map)
            print('b')

    def __init__(self, game):
        super().__init__(game)
        btn_new_game = Button(4, 4, 30, 5)
        self.add_render(btn_new_game)
        self.ui_map = [[btn_new_game]]
        self.add_render(Border(Back.CYAN + ' ' + Back.RESET))
        self.listener = keyboard.Listener(on_release=self.on_release)

    def start(self):
        self.listener.start()

    def update(self):
        pass