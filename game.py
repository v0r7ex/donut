from button import Button
from donut import Donut
from level import Level

class Game():
    def __init__(self):
        self.load_images()
        self.create_buttons()
        self.resize_images()
        self.donut = Donut()
        self.build_level0()
        self.current_level = None
        
    def load_images(self):
        self.dirt_block_img = loadImage(

    def resize_images(self):
        self.bkgd_img.resize(width, height)
        
    def create_buttons(self):
        pass
        
    def build_level0(self):
        self.level0_bkgd_img = loadImage("level/sky_blue.png")
        self.level0_bkgd_img.resize(width, height)
        self.level0 = Level(self.donut, 100, self.level0_bkgd_img)
        
    def reset(self):
        frameRate(30)
        self.current_level = None

    def display(self):
        self.current_level.display()
        
    def click(self):
        pass
