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
        self.current_level_completed = False
        
    def load_images(self):
        self.dirt_tile_img = loadImage("level/dirt.png")
        self.grass_tile_img = loadImage("level/grass.png")
        self.stone_tile_img = loadImage("level/stone.png")
        self.ditch_tile_img = loadImage("level/ditch.png")
        self.flower1_img = loadImage("level/flower1.png")
        self.flower2_img = loadImage("level/flower2.png")
        self.flower3_img = loadImage("level/flower3.png")
        self.check_point1_img = loadImage("level/checkpoint1.png")
        self.check_point2_img = loadImage("level/checkpoint2.png")
        
    def resize_images(self):
        self.dirt_tile_img.resize(self.tile_size, self.tile_size)
        self.grass_tile_img.resize(self.tile_size, self.tile_size)
        self.stone_tile_img.resize(self.tile_size, self.tile_size)
        self.ditch_tile_img.resize(self.tile_size, self.tile_size)
        self.flower1_img.resize(self.tile_size, self.tile_size)
        self.flower2_img.resize(self.tile_size, self.tile_size)
        self.flower3_img.resize(self.tile_size, self.tile_size)        
        self.check_point1_img.resize(self.tile_size, self.tile_size)
        self.check_point2_img.resize(self.tile_size, self.tile_size)
        

    def build_level0(self, usable_keys):
        self.level0_bkgd_img = loadImage("level/sky.png")
        self.level0_bkgd_img.resize(width, height)
        self.level0 = Level(self.donut, self.tile_size, usable_keys, 240, self.level0_bkgd_img, self.check_point2_img, 4)
        self.level0.build_platform(0, 12, 11, self.dirt_tile_img, False)
        self.level0.build_platform(0, 11, 11, self.grass_tile_img)
        self.level0.build_platform(1, 10, 0, self.flower1_img, False)
        self.level0.build_platform(2, 10, 0, self.flower2_img, False)
        self.level0.build_platform(12, 12, 2, self.ditch_tile_img, False)
        self.level0.build_platform(15, 12, 10, self.dirt_tile_img, False)
        self.level0.build_platform(15, 11, 10, self.grass_tile_img)
        self.level0.build_platform(20, 8, 3, self.stone_tile_img, True, True) 
        self.level0.build_platform(24, 10, 0, self.flower2_img, False)
        self.level0.build_platform(27, 6, 3, self.stone_tile_img, True, True)
        self.level0.build_platform(33, 4, 4, self.stone_tile_img, True, True)
        self.level0.build_platform(34, 3, 0, self.check_point1_img, False, False, True, 1)
        self.level0.build_platform(42, 4, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(46, 4, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(50, 4, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(54, 4, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(55, 4, 3, self.grass_tile_img)
        self.level0.build_platform(58, 3, 0, self.flower2_img, False)
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
        self.level0.build_platform(81, 10, 0, self.flower3_img, False)
        self.level0.build_platform(93, 12, 2, self.dirt_tile_img, False)
        self.level0.build_platform(93, 11, 2, self.grass_tile_img)
        self.level0.build_platform(95, 10, 0, self.flower2_img, False)
        self.level0.build_platform(100, 12, 2, self.dirt_tile_img, False)
        self.level0.build_platform(100, 11, 2, self.grass_tile_img)
        self.level0.build_platform(107, 12, 8, self.dirt_tile_img, False)
        self.level0.build_platform(107, 11, 8, self.grass_tile_img)
        self.level0.build_platform(113, 10, 0, self.flower1_img, False)
        self.level0.build_platform(113, 8, 2, self.stone_tile_img, True, True)
        self.level0.build_platform(113, 5, 2, self.stone_tile_img, True, True)
        self.level0.build_platform(113, 2, 2, self.stone_tile_img, True, True)
        self.level0.build_platform(118, 2, 5, self.stone_tile_img, True, True)
        self.level0.build_platform(121, 1, 0, self.check_point1_img, False, False, True, 2)
        self.level0.build_platform(125, 4, 3, self.stone_tile_img, True, True)
        self.level0.build_platform(130, 1, 7, self.stone_tile_img, True, True)
        self.level0.build_platform(132, 0, 0, self.flower1_img, False)
        self.level0.build_platform(137, 5, 1, self.stone_tile_img, True, True)
        self.level0.build_platform(142, 6, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(146, 7, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(150, 8, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(154, 9, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(158, 11, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(162, 9, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(166, 11, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(170, 9, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(170, 8, 0, self.flower2_img, False)
        self.level0.build_platform(174, 11, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(178, 11, 3, self.grass_tile_img)
        self.level0.build_platform(178, 12, 3, self.dirt_tile_img, False)
        self.level0.build_platform(181, 8, 4, self.grass_tile_img)
        self.level0.build_platform(181, 9, 4, self.dirt_tile_img, False)
        self.level0.build_platform(181, 10, 4, self.dirt_tile_img, False)
        self.level0.build_platform(182, 11, 3, self.dirt_tile_img, False)
        self.level0.build_platform(182, 12, 3, self.dirt_tile_img, False)
        self.level0.build_platform(184, 7, 0, self.check_point1_img, False, False, True, 3)
        self.level0.build_platform(180, 5, 2, self.grass_tile_img)
        self.level0.build_platform(180, 6, 2, self.dirt_tile_img, False)
        self.level0.build_platform(180, 7, 2, self.dirt_tile_img, False)
        self.level0.build_platform(180, 8, 0, self.dirt_tile_img, False)
        self.level0.build_platform(180, 9, 0, self.dirt_tile_img, False)
        self.level0.build_platform(180, 10, 0, self.dirt_tile_img, False)
        self.level0.build_platform(182, 4, 0, self.flower3_img, False)
        self.level0.build_platform(186, 12, 0, self.ditch_tile_img, False)
        self.level0.build_platform(187, 3, 4, self.grass_tile_img)
        self.level0.build_platform(187, 4, 4, self.dirt_tile_img, False)
        self.level0.build_platform(187, 5, 4, self.dirt_tile_img, False)
        self.level0.build_platform(187, 6, 4, self.dirt_tile_img, False)
        self.level0.build_platform(187, 7, 4, self.dirt_tile_img, False)
        self.level0.build_platform(187, 8, 4, self.dirt_tile_img, False)
        self.level0.build_platform(187, 9, 4, self.dirt_tile_img, False)
        self.level0.build_platform(187, 10, 4, self.dirt_tile_img, False)
        self.level0.build_platform(187, 11, 4, self.dirt_tile_img, False)
        self.level0.build_platform(187, 12, 4, self.dirt_tile_img, False)
        self.level0.build_platform(192, 12, 2, self.ditch_tile_img, False)
        self.level0.build_platform(195, 3, 4, self.grass_tile_img)
        self.level0.build_platform(195, 4, 4, self.dirt_tile_img, False)
        self.level0.build_platform(195, 5, 4, self.dirt_tile_img, False)
        self.level0.build_platform(195, 6, 4, self.dirt_tile_img, False)
        self.level0.build_platform(195, 7, 4, self.dirt_tile_img, False)
        self.level0.build_platform(195, 8, 4, self.dirt_tile_img, False)
        self.level0.build_platform(195, 9, 4, self.dirt_tile_img, False)
        self.level0.build_platform(195, 10, 4, self.dirt_tile_img, False)
        self.level0.build_platform(195, 11, 4, self.dirt_tile_img, False)
        self.level0.build_platform(195, 12, 4, self.dirt_tile_img, False)
        self.level0.build_platform(200, 4, 1, self.grass_tile_img)
        self.level0.build_platform(200, 5, 1, self.dirt_tile_img, False)
        self.level0.build_platform(200, 6, 1, self.dirt_tile_img, False)
        self.level0.build_platform(200, 7, 1, self.dirt_tile_img, False)
        self.level0.build_platform(200, 8, 1, self.dirt_tile_img, False)
        self.level0.build_platform(200, 9, 1, self.dirt_tile_img, False)
        self.level0.build_platform(200, 10, 1, self.dirt_tile_img, False)
        self.level0.build_platform(200, 11, 1, self.dirt_tile_img, False)
        self.level0.build_platform(200, 12, 1, self.dirt_tile_img, False)
        self.level0.build_platform(202, 5, 1, self.grass_tile_img)
        self.level0.build_platform(202, 6, 1, self.dirt_tile_img, False)
        self.level0.build_platform(202, 7, 1, self.dirt_tile_img, False)
        self.level0.build_platform(202, 8, 1, self.dirt_tile_img, False)
        self.level0.build_platform(202, 9, 1, self.dirt_tile_img, False)
        self.level0.build_platform(202, 10, 1, self.dirt_tile_img, False)
        self.level0.build_platform(202, 11, 1, self.dirt_tile_img, False)
        self.level0.build_platform(202, 12, 1, self.dirt_tile_img, False)
        self.level0.build_platform(204, 6, 1, self.grass_tile_img)
        self.level0.build_platform(204, 7, 1, self.dirt_tile_img, False)
        self.level0.build_platform(204, 8, 1, self.dirt_tile_img, False)
        self.level0.build_platform(204, 9, 1, self.dirt_tile_img, False)
        self.level0.build_platform(204, 10, 1, self.dirt_tile_img, False)
        self.level0.build_platform(204, 11, 1, self.dirt_tile_img, False)
        self.level0.build_platform(204, 12, 1, self.dirt_tile_img, False)
        self.level0.build_platform(206, 7, 1, self.grass_tile_img)
        self.level0.build_platform(206, 8, 1, self.dirt_tile_img, False)
        self.level0.build_platform(206, 9, 1, self.dirt_tile_img, False)
        self.level0.build_platform(206, 10, 1, self.dirt_tile_img, False)
        self.level0.build_platform(206, 11, 1, self.dirt_tile_img, False)
        self.level0.build_platform(206, 12, 1, self.dirt_tile_img, False)
        self.level0.build_platform(208, 8, 1, self.grass_tile_img)
        self.level0.build_platform(208, 9, 1, self.dirt_tile_img, False)
        self.level0.build_platform(208, 10, 1, self.dirt_tile_img, False)
        self.level0.build_platform(208, 11, 1, self.dirt_tile_img, False)
        self.level0.build_platform(208, 12, 1, self.dirt_tile_img, False)
        self.level0.build_platform(210, 9, 1, self.grass_tile_img)
        self.level0.build_platform(210, 8, 0, self.flower2_img, False)
        self.level0.build_platform(210, 10, 1, self.dirt_tile_img, False)
        self.level0.build_platform(210, 11, 1, self.dirt_tile_img, False)
        self.level0.build_platform(210, 12, 1, self.dirt_tile_img, False)
        self.level0.build_platform(212, 10, 1, self.grass_tile_img)
        self.level0.build_platform(212, 11, 1, self.dirt_tile_img, False)
        self.level0.build_platform(212, 12, 1, self.dirt_tile_img, False)
        self.level0.build_platform(214, 11, 25, self.grass_tile_img)
        self.level0.build_platform(214, 12, 25, self.dirt_tile_img, False)
        self.level0.build_platform(219, 10, 2, self.stone_tile_img, True, True)
        self.level0.build_platform(220, 9, 0, self.stone_tile_img, True, True)
        self.level0.build_platform(220, 8, 0, self.check_point1_img, False, False, True, 4)        
        
    def reset(self):
        self.current_level = None
        self.current_level_completed = False
        
    def reset_donut(self):
        self.current_level.donut.img_x = width/10
        self.current_level.donut.img_y = 0
        self.current_level.donut.box_x = (self.current_level.donut.img_x + self.current_level.donut.img_width/2) - self.current_level.donut.tile_size/2
        self.current_level.donut.box_y = int(self.current_level.donut.img_y + 0.15 * self.current_level.donut.img_height)
        self.current_level.donut.x_velocity = 0
        self.current_level.donut.y_velocity = 0
        self.current_level.donut.state = "stand"
        self.current_level.donut.direction = "right"
        self.current_level.donut.active_jump = False
        self.current_level.donut.frames_since_land = 0
        self.current_level.donut.falling_through = False
        self.current_level.donut.current_frame = 0
        self.current_level.donut.dead = False
        self.current_level.donut.coma_frames = 0
        
    def reset_current_level(self):
        self.reset_donut()
        self.current_level.tile_scroll_pos = 0
        self.current_level.last_check_point = 0
        self.current_level.level_completed = False
        for i in range(len(self.current_level.grid)):
            for k in range(len(self.current_level.grid[i])):
                if self.current_level.grid[i][k].check_point == True:
                    self.current_level.grid[i][k].img = self.check_point1_img
                if self.current_level.grid[0][0].on_screen() is False:
                    for i in range(len(self.current_level.grid)):
                        for k in range(len(self.current_level.grid[i])):
                            self.current_level.grid[i][k].x += self.current_level.tile_size
                

    def display(self):
        level_complete = self.current_level_completed = self.current_level.display()
        if level_complete == True:
            self.reset_current_level()
        
    def click(self):
        self.current_level.click()
