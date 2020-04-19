from Code.IRenderObject import IRenderObject


class IUserInterface(IRenderObject):
    def on_overlap(self, target):
        pass

    def on_click(self, target):
        pass

    def darw(self, target):
        pass
