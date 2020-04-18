class Canvas:
    def __init__(self, size_x=100, size_y=100):
        self.sizeX = size_x
        self.sizeY = size_y
        self.commandDrawer = []
        self.create_image(size_x, size_y)
        self.symphol = '.'

    def set_size(self, size_x, size_y):
        self.sizeX = size_x
        self.sizeY = size_y

    def set_symphol(self, sym='.'):
        self.symphol = str(sym)

    def create_image(self, sizeX, sizeY):
        self.imageCanvas = [[' '] * sizeX for i in range(sizeY)]

    def Point(self, x, y):
        self.commandDrawer.append({'point': [x, y]})

    def Line(self, x, y, x1, y1):
        self.commandDrawer.append({'line': [x, y, x1, y1]})

    def Circle(self, x, y, r):
        self.commandDrawer.append({'circle': [x, y, r]})

    def Rectangle(self, x, y, x1, y1):
        self.commandDrawer.append({'rectangle': [x, y, x1, y1]})

    def draw(self):
        for i in self.commandDrawer:
            if i.get('point'):
                coords = i.get('point')
                self.drawPoint(coords[0], coords[1])
            elif i.get('line'):
                coords = i.get('line')
                self.drawLine(coords[0], coords[1], coords[2], coords[3])
            elif i.get('circle'):
                coords = i.get('circle')
                pass
        for i in self.imageCanvas:
            print(''.join(i))

    def drawPoint(self, x, y):
        self.imageCanvas[x][y] = self.symphol

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
