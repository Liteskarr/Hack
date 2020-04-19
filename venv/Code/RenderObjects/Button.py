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
        self.border_char = Back.LIGHTWHITE_EX+ ' ' + Back.RESET
        self.fill_char = Back.BLACK + ' ' + Back.RESET

    def darw(self, target):
        target.fill_rect(self.x1 + 1, self.y1 + 1, self.sizeX - 2, self.sizeY - 2, self.fill_char)
        target.add_rect(self.x1, self.y1, self.sizeX, self.sizeY, self.border_char)
        target.add_text(self.x1 + 2, (2 * self.y1 + self.sizeY) // 2,
                        len(self.text), 1, self.text)