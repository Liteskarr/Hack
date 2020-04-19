import threading
import os
import msvcrt

from Code.Canvas import Canvas


class Game:
    def __init__(self, canvas=Canvas(100, 50)):
        self.is_run = True
        self.loaded_scene = None
        self.canvas = canvas

    def load_scene(self, scene):
        self.loaded_scene = scene

    def draw(self):
        os.system(f'mode con cols={self.canvas.sizeX} lines={self.canvas.sizeY}')
        os.system('cls')
        for rend in self.loaded_scene:
            self.canvas(rend)

    def start(self):
        if self.loaded_scene is None:
            print('Сцена не загружена!')
            return

        while self.is_run:
            self.loaded_scene.update()
            draw()
