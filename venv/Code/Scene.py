from collections import defaultdict

import Code.Canvas as Canvas
import Code.IRenderObject as IRenderObject


class Scene:
    def __init__(self):
        self.data = {}
        self.data['renders'] = []

    def get_renders(self):
        return self.data['renders']

    def add_render(self, obj: IRenderObject.IRenderObject):
        self.data['renders'].append(obj)