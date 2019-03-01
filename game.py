from button import Button
from donut import Donut
from level import Level

class Game():
    def __init__(self):
        self.tile_size = int(7.7 * height/100)
        self.load_images()
        self.resize_images()
        self.donut = Donut()
        self.build_level0()
        self.current_level = None
        
    def load_images(self):
        self.dirt_tile_img = loadImage("level/dirt.png")
        self.grass_tile_img = loadImage("level/grass.png")
        self.stone_tile_img = loadImage("level/stone.png")
        self.wood_tile_img = loadImage("level/wood.png")
        
    def resize_images(self):
        self.dirt_tile_img.resize(self.tile_size, self.tile_size)
        self.grass_tile_img.resize(self.tile_size, self.tile_size)
        self.stone_tile_img.resize(self.tile_size, self.tile_size)
        self.wood_tile_img.resize(self.tile_size, self.tile_size)
        
    def build_level0(self):
        self.level0_bkgd_img = loadImage("level/sky_blue.png")
        self.level0_bkgd_img.resize(width, height)
        self.level0 = Level(self.donut, self.tile_size, 200, self.level0_bkgd_img)
        self.level0.build_platform(0, 12, 14, self.dirt_tile_img)
        self.level0.build_platform(0, 11, 14, self.grass_tile_img)
        self.level0.build_platform(10, 8, 3, self.stone_tile_img)        
        self.level0.build_platform(18, 12, 10, self.dirt_tile_img)
        self.level0.build_platform(18, 11, 10, self.grass_tile_img)
        
    def reset(self):
        frameRate(16)
        self.current_level = None

    def display(self):
        self.current_level.display()
        
    def click(self):
        self.current_level.click()
