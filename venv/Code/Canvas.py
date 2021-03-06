from collections import defaultdict
from Code.IRenderObject import IRenderObject


class Canvas:
    def __init__(self, size_x, size_y, fill=' '):
        self.sizeX = size_x
        self.sizeY = size_y
        self.fill_char = fill
        self.chars = defaultdict(lambda: fill)

    def resize(self, size_x, size_y):
        self.sizeX = size_x
        self.sizeY = size_y

    def set_fillchar(self, fillchar):
        self.fill_char = fillchar
        self.chars.default_factory = lambda: fillchar

    def add_char(self, x, y, char):
        self.chars[x, y] = char

    def add_line(self, x1, y1, x2, y2, char):
        dx = x2 - x1
        dy = y2 - y1

        dmax = abs(max(dx, dy))
        dx /= dmax
        dy /= dmax

        x = x1
        y = y1
        gx = round(x)
        gy = round(y)

        while x1 <= gx <= x2 and y1 <= gy <= y2:
            self.chars[gx, gy] = char
            x += dx
            y += dy
            gx = round(x)
            gy = round(y)

    def add_rect(self, x0, y0, size_x, size_y, char):
        self.add_line(x0, y0, x0 + size_x, y0, char)
        self.add_line(x0, y0, x0, y0 + size_y, char)
        self.add_line(x0 + size_x, y0, x0 + size_x, y0 + size_y, char)
        self.add_line(x0, y0 + size_y, x0 + size_x, y0 + size_y, char)

    def add_object(self, obj: IRenderObject):
        obj.darw(self)

    def fill_rect(self, x1, y1, sizeX, sizeY, char):
        for x in range(x1, x1 + sizeX + 1):
            for y in range(y1, y1 + sizeY + 1):
                self.chars[x, y] = char

    def add_text(self, x1, y1, sizeX, sizeY, text):
        x = x1
        y = y1
        for char in text:
            self.chars[x, y] = char
            x += 1
            if x >= x1 + sizeX:
                y += 1
                x = x1

            if y >= y1 + sizeY:
                return

    def clear(self):
        self.chars = defaultdict(lambda: self.fill_char)

    def draw(self):
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                print(self.chars[x, y], end='')
            print()
