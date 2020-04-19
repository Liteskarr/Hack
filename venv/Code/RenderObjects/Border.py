import Code.IRenderObject as IRenderObject


class Border(IRenderObject.IRenderObject):
    def __init__(self, char):
        self.char = char

    def darw(self, target):
        target.add_rect(0, 0, target.sizeX - 1, target.sizeY - 1, self.char)