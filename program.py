from menu import Menu
from settings_state import Settings
from about import About
from pause import Pause
from game import Game
from level_select import Level_Select
from level_end import Level_End

class Program():
    def __init__(self):
        self.menu = Menu()
        self.settings_state = Settings()
        self.about = About()
        self.pause = Pause()
        self.game = Game()
        self.level_end = Level_End()
        self.level_select = Level_Select()
        self.gs_dict = {
                        "menu": self.menu,
                        "settings": self.settings_state,
                        "about": self.about,
                        "pause": self.pause,
                        "game": self.game,
                        "level_end": self.level_end,
                        "level_select": self.level_select
                        }
        self.level_dict = {
                           "level0": self.game.level0
                           }
        self.gs = self.menu
        self.menu_soundtrack = None #sounds loaded in setup()
        self.game_soundtrack = None
        self.current_soundtrack = None
        
    def check_soundtrack(self):
        new_soundtrack = None
        if self.gs == self.menu or self.gs == self.settings_state or self.gs == self.about or self.gs == self.level_select:
            if self.current_soundtrack is not self.menu_soundtrack:
                new_soundtrack = self.menu_soundtrack
        elif self.gs == self.game or self.gs == self.pause or self.gs == self.level_end:
            if self.current_soundtrack is not self.game_soundtrack:
                new_soundtrack = self.game_soundtrack
        else:
            print "c"
        if new_soundtrack is not None: #shiftGain() gradually changes the volume
            self.current_soundtrack.shiftGain(0, -50, 400)
            delay(400)
            self.current_soundtrack.pause()
            self.current_soundtrack = new_soundtrack
            self.current_soundtrack.loop()
            self.current_soundtrack.shiftGain(-50, 0, 700)
        
    def display(self):
        self.gs.display()
        
    def click(self):
        result = self.gs.click()
        if result is not None:
            if self.gs is self.level_select:
                if result in self.level_dict:
                    self.gs = self.game
                    self.gs.reset()
                    self.game.current_level = self.level_dict[result]    
            else:
                self.gs = self.gs_dict[result]
                self.gs.reset()
            self.check_soundtrack()
