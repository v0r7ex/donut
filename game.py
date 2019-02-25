from button import Button
from donut import Donut
from level import Level

class Game():
    def __init__(self):
        self.block_size = int(5 * width/100)
        self.load_images()
        self.resize_images()
        self.donut = Donut()
        self.build_level0()
        self.current_level = None
        
    def load_images(self):
        self.dirt_block_img = loadImage("level/dirt.png")
        self.grass_block_img = loadImage("level/grass.png")
        self.stone_block_img = loadImage("level/stone.png")
        self.wood_block_img = loadImage("level/wood.png")
        
    def resize_images(self):
        self.dirt_block_img.resize(self.block_size, self.block_size)
        self.grass_block_img.resize(self.block_size, self.block_size)
        self.stone_block_img.resize(self.block_size, self.block_size)
        self.wood_block_img.resize(self.block_size, self.block_size)
        
    def build_level0(self):
        self.level0_bkgd_img = loadImage("level/sky_blue.png")
        self.level0_bkgd_img.resize(width, height)
        self.level0 = Level(self.donut, self.block_size, 142, self.level0_bkgd_img)
        
    def reset(self):
        frameRate(30)
        self.current_level = None

    def display(self):
        self.current_level.display()
        
    def click(self):
        self.current_level.click()
