from collections import defaultdict


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

    def add_line(self, x1, y1, x2, y2):


    def draw(self):
        for x in range(self.sizeX):
            for y in range(self.sizeY):
                print(defaultdict)

    def drawLine(self, x, y, x1, y1):
        if x == x1 and y1 != y:
            for cordY in range(y, y1 + 1):
                self.drawPoint(x, cordY)
        elif y1 == y and x1 != x:
            for cordX in range(x, x1 + 1):
                self.drawPoint(cordX, y)
        else:
            k = (y1 - y) / (x1 - x)
            b = y - k * x
            for cordX in range(x, x1 + 1):
                self.drawPoint(cordX, int((k * cordX) + b))
