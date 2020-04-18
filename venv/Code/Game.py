import threading
import os


class Game:
    def __int__(self):
        self.draw_thread = None
        self.input_thread = None
        self.update_thread = None

    def set_draw(self, func):
        self.draw_thread = threading.Thread(target=func)

    def set_input(self, func):
        self.input_thread = threading.Thread(target=func)

    def set_update(self, func):
        self.update_thread = threading.Thread(target=func)

    def start(self):
        self.draw_thread.start()
        self.input_thread.start()
        self.update_thread.start()

    def join(self):
        self.draw_thread.join()
        self.update_thread.join()
        self.input_thread.join()
