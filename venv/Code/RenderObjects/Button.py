from Code.IRenderObject import IRenderObject
from colorama import Back

class Button(IRenderObject):
    def __init__(self, x1, y1, sizeX, sizeY, text='', on_click=None, on_overlap=None):
        self.x1 = x1
        self.y1 = y1
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.text = text
        self.on_click = on_click
        self.on_overlap = on_overlap
        self.border_char = '#'
        self.fill_char = Back.BLACK + ' ' + Back.RESET

    def darw(self, target):
        target.add_rect(self.x1, self.y1, self.sizeX, self.sizeY, self.border_char)
        target.fill_rect(self.x1 + 1, self.y1 + 1, self.sizeX - 1, self.sizeY - 1, self.fill_char)
        target.add_text()