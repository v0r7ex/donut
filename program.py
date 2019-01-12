from menu import Menu
from credits import Credits
from pause import Pause
from game import Game
from level_end import Level_End

class Program():
    def __init__(self):
        self.menu = Menu()
        self.credits = Credits()
        self.pause = Pause()
        self.game = Game
        self.level_end = Level_End()
        
        self.gs = self.menu
        
    def display(self):
        self.gs.display()
