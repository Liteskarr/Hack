import os
import threading
#
import colorama
from colorama import Back
#
from Code.Game import Game
from Code.Scenes.MainMenu import MainMenu
from Code.Mp3player import Mp3player
#
colorama.init()

game = Game()
game.load_scene(MainMenu(game))
game.start()
