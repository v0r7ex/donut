from menu import Menu
from help import Help
from credits import Credits
from pause import Pause
from game import Game
from level_end import Level_End

class Program():
    def __init__(self):
        self.menu = Menu()
        self.help = Help()
        self.credits = Credits()
        self.pause = Pause()
        self.game = Game()
        self.level_end = Level_End()
        self.gs_dict = {
                        "menu": self.menu,
                        "help": self.help,
                        "credits": self.credits,
                        "pause": self.pause,
                        "game": self.game,
                        "level_end": self.level_end
                        }
        self.gs = self.menu
        
    def display(self):
        self.gs.display()
        
    def click(self):
        result = self.gs.click()
        if result is not None:
            self.gs = self.gs_dict[result]
