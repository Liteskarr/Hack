from collections import defaultdict

import Code.Canvas as Canvas
import Code.IRenderObject as IRenderObject


class Scene:
    def __init__(self, game):
        self.game = game
        self.renders = []
        self.ui_map = []
        self.listener = None

    def add_render(self, obj):
        self.renders.append(obj)

    def set_ui_map(self, ui_map):
        self.ui_map = ui_map

    def get_ui(self, x, y):
        return self.ui_map[x][y]

    def update(self):
        pass

    def start(self):
        pass