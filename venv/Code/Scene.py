from collections import defaultdict

import Code.Canvas as Canvas
import Code.IRenderObject as IRenderObject


class Scene:
    def __init__(self):
        self.drawing_rules = defaultdict(list)
        self.data = {}
        self.data['renders'] = []

    def get_renders(self):
        return self.data['renders']

    def add_render(self, obj: IRenderObject.IRenderObject):
        self.data['renders'].append(obj)

    def add_draw(self, name, rule: dict):
        self.drawing_rules[name].append(rule)

    def get_rule(self, cond):

