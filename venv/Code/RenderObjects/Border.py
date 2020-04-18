import Code.IRenderObject as IRenderObject


class Border(IRenderObject.IRenderObject):
    def __init__(self, char):
        self.char = char

    @override
    def darw(self, target: Canvas):
        target.set_symphol(self.char)
        target.Line(0, 0, target.sizeX, 0)
        target.Line(0, 0, 0, target.sizeY)
        target.Line(target.sizeX, 0, target.sizeX, target.sizeY)
        target.Line(0, target.sizeY, target.sizeX, target.sizeY)