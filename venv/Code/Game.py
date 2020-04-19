import threading
import os

import keyboard

from Code.Canvas import Canvas


class Game:
    def __init__(self, canvas=Canvas(100, 45)):
        self.is_run = True
        self.loaded_scene = None
        self.canvas = canvas

    def load_scene(self, scene):
        self.loaded_scene = scene
        keyboard.hook(scene.listen_clicks)
        scene.start()

    def draw(self):
        os.system(f'mode con cols={self.canvas.sizeX} lines={self.canvas.sizeY + 1}')
        os.system('cls')
        for rend in self.loaded_scene.renders:
            self.canvas.add_object(rend)
        self.canvas.draw()

    def start(self):
        if self.loaded_scene is None:
            print('Сцена не загружена!')
            return

        while self.is_run:
            self.loaded_scene.update()
            self.draw()
