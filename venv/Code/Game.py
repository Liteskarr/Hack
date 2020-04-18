import threading


class Game:
    def __init__(self):
        self.input_thread = None
        self.draw_thread = None

    def set_input(self, func):
        self.input_thread = threading.Thread(target=func)

    def set_draw(self, func):
        self.draw_thread = threading.Thread(target=func)
