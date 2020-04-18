import Code.IRenderObject as IRenderObject


class Border(IRenderObject.IRenderObject):
    def __init__(self, char):
        self.char = char

    def darw(self, target):
        target.add_line(0, 0, target.sizeX, 0, self.char)