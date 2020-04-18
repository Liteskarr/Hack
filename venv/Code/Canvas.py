class Canvas:
    def __init__(self, size_x=100, size_y=100):
        self.sizeX = size_x
        self.sizeY = size_y
        self.commandConsole = []
        self.create_image(size_x, size_y)
        self.symphol = '.'

    def set_size(self, size_x, size_y):
        self.sizeX = size_x
        self.sizeY = size_y

    def set_symphol(self, sym='.'):
        self.symphol = str(sym)

    def give_command(self, x, y):
        self.commandConsole.append([x, y])

    def create_image(self, sizeX, sizeY):
        self.imageHolst = [[''] * sizeX for i in range(sizeY)]

    def draw(self):
        for i in self.commandConsole:
            self.imageHolst[i[0]][i[1]] = self.symphol
        for i in self.imageHolst:
            print(''.join(i))
