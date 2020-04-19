import os
#
import colorama
from colorama import Back
#
from Code.Game import Game
from Code.Scenes.MainMenu import main_menu
#
colorama.init()

def default_update():
    os.system("mode con cols=100 lines=49")

default_update()

game = Game()
game.load_scene(main_menu)
game.start()
game.join()