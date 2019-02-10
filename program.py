from menu import Menu
from settings_state import Settings
from about import About
from pause import Pause
from game import Game
from level_end import Level_End

class Program():
    def __init__(self):
        self.menu = Menu()
        self.settings_state = Settings()
        self.about = About()
        self.pause = Pause()
        self.game = Game()
        self.level_end = Level_End()
        self.gs_dict = {
                        "menu": self.menu,
                        "settings": self.settings_state,
                        "about": self.about,
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
            self.gs.reset()
