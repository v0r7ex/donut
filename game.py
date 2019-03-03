from button import Button
from donut import Donut
from level import Level

class Game():
    def __init__(self, usable_keys):
        self.tile_size = int(7.7 * height/100) + 1
        self.load_images()
        self.resize_images()
        self.donut = Donut(self.tile_size)
        self.build_level0(usable_keys)
        self.current_level = None
        
    def load_images(self):
        self.dirt_tile_img = loadImage("level/dirt.png")
        self.grass_tile_img = loadImage("level/grass.png")
        self.stone_tile_img = loadImage("level/stone.png")
        self.ditch_tile_img = loadImage("level/ditch.png")
        self.flower1_img = loadImage("level/flower1.png")
        self.check_point1_img = loadImage("level/checkpoint1.png")
        self.check_point2_img = loadImage("level/checkpoint2.png")
        
    def resize_images(self):
        self.dirt_tile_img.resize(self.tile_size, self.tile_size)
        self.grass_tile_img.resize(self.tile_size, self.tile_size)
        self.stone_tile_img.resize(self.tile_size, self.tile_size)
        self.ditch_tile_img.resize(self.tile_size, self.tile_size)
        self.flower1_img.resize(self.tile_size, self.tile_size)        
        self.check_point1_img.resize(self.tile_size, self.tile_size)
        self.check_point2_img.resize(self.tile_size, self.tile_size)
        

    def build_level0(self, usable_keys):
        self.level0_bkgd_img = loadImage("level/sky.png")
        self.level0_bkgd_img.resize(width, height)
        self.level0 = Level(self.donut, self.tile_size, usable_keys, 400, self.level0_bkgd_img, self.check_point2_img)
        self.level0.build_platform(0, 12, 12, self.dirt_tile_img, False)
        self.level0.build_platform(0, 11, 12, self.grass_tile_img)
        self.level0.build_platform(1, 10, 0, self.flower1_img, False)
        self.level0.build_platform(16, 10, 0, self.flower1_img, False)
        self.level0.build_platform(13, 12, 2, self.ditch_tile_img, False)       
        self.level0.build_platform(15, 12, 10, self.dirt_tile_img, False)
        self.level0.build_platform(15, 11, 10, self.grass_tile_img)
        self.level0.build_platform(20, 8, 3, self.stone_tile_img, True, True) 
        self.level0.build_platform(23, 10, 0, self.flower1_img, False)
        self.level0.build_platform(27, 6, 3, self.stone_tile_img, True, True)
        self.level0.build_platform(33, 4, 4, self.stone_tile_img, True, True)
        self.level0.build_platform(34, 3, 0, self.check_point1_img, False, False, True)
        self.level0.build_platform(42, 4, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(46, 4, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(50, 4, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(54, 4, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(55, 4, 3, self.grass_tile_img)
        self.level0.build_platform(57, 3, 0, self.flower1_img, False)
        self.level0.build_platform(55, 5, 3, self.dirt_tile_img, False)
        self.level0.build_platform(55, 6, 5, self.dirt_tile_img, False)
        self.level0.build_platform(55, 7, 7, self.dirt_tile_img, False)
        self.level0.build_platform(55, 8, 9, self.dirt_tile_img, False)
        self.level0.build_platform(55, 9, 11, self.dirt_tile_img, False)
        self.level0.build_platform(55, 10, 13, self.dirt_tile_img, False)
        self.level0.build_platform(55, 11, 15, self.dirt_tile_img, False)
        self.level0.build_platform(55, 12, 17, self.dirt_tile_img, False)
        self.level0.build_platform(59, 5, 1, self.grass_tile_img)
        self.level0.build_platform(61, 6, 1, self.grass_tile_img)
        self.level0.build_platform(63, 7, 1, self.grass_tile_img)
        self.level0.build_platform(65, 8, 1, self.grass_tile_img)
        self.level0.build_platform(67, 9, 1, self.grass_tile_img)
        self.level0.build_platform(69, 10, 1, self.grass_tile_img)
        self.level0.build_platform(71, 11, 1, self.grass_tile_img)
        self.level0.build_platform(79, 12, 2, self.dirt_tile_img, False)
        self.level0.build_platform(79, 11, 2, self.grass_tile_img)
        self.level0.build_platform(86, 12, 2, self.dirt_tile_img, False)
        self.level0.build_platform(86, 11, 2, self.grass_tile_img)
        self.level0.build_platform(88, 10, 0, self.flower1_img, False)
        self.level0.build_platform(93, 12, 2, self.dirt_tile_img, False)
        self.level0.build_platform(93, 11, 2, self.grass_tile_img)
        self.level0.build_platform(100, 12, 2, self.dirt_tile_img, False)
        self.level0.build_platform(100, 11, 2, self.grass_tile_img)
        self.level0.build_platform(107, 12, 8, self.dirt_tile_img, False)
        self.level0.build_platform(107, 11, 8, self.grass_tile_img)
        self.level0.build_platform(113, 10, 0, self.flower1_img, False)
        
        


        
    def reset(self):
        self.current_level = None

    def display(self):
        self.current_level.display()
        
    def click(self):
        self.current_level.click()
