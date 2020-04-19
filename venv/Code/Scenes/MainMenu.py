import Code.Scene as Scene
from Code.RenderObjects.Border import Border
from Code.RenderObjects.Button import Button

from colorama import Back



class MainMenu(Scene.Scene()):
    def __init__(self):
        pass

    def update(self):
        pass

    def


main_menu = Scene.Scene()
main_menu.add_render(Border(Back.CYAN + ' ' + Back.RESET))

new_game = Button(1, 1, 5, 20)
authors = Button(1, 1, 5, 20)
leave = Button(1, 1, 5, 20)

ui_map = [[new_game], [authors], [leave]]