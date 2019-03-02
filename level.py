from button import Button
from tile import Tile

class Level():
    def __init__(self, donut, tile_size, usable_keys, width_in_tiles, background_img):
        self.donut = donut
        self.tile_size = tile_size
        self.usable_keys = usable_keys
        self.width_in_tiles = width_in_tiles
        self.height_in_tiles = 13
        self.grid = [[None] * self.height_in_tiles for _ in range(self.width_in_tiles)]
        self.populate_grid()
        self.bkgd_img = background_img
        self.load_images()
        self.create_buttons()
        self.resize_images()
        self.tile_scroll_pos = 0 #tile_scoll_pos and render_width_in_tiles are used to select a portion of the grid to iterate through when displaying
        self.render_width_in_tiles = 30
        
    def load_images(self):
        pass
        
    def resize_images(self):
        pass
    
    def create_buttons(self):
        pass
        
    def populate_grid(self):
        for i in range(len(self.grid)):
            for k in range(len(self.grid[i])):
                self.grid[i][k] = Tile(i * self.tile_size, k * self.tile_size, self.tile_size, None, False, False)
                
    def build_platform(self, i_coord, k_coord, length_in_tiles, img, solid = True, fall_through = False, check_point = False):
        for i in range(i_coord, i_coord + length_in_tiles + 1):
            self.grid[i][k_coord].img = img
            self.grid[i][k_coord].solid = solid
            self.grid[i][k_coord].fall_through = fall_through
            self.grid[i][k_coord].check_point = check_point
            
    def donut_at_solid(self, check_bottom = True, check_top = True, return_tile = False):
        grid_render_end = self.tile_scroll_pos + self.render_width_in_tiles if self.tile_scroll_pos + self.render_width_in_tiles < len(self.grid) else len(self.grid) - 1
        for i in range(self.tile_scroll_pos, grid_render_end):
            for k in range(len(self.grid[i])):
                if check_bottom is True:
                    if (self.donut.coord_in_bottom(self.grid[i][k].x, self.grid[i][k].y) is True or self.donut.coord_in_bottom(self.grid[i][k].x + self.tile_size, self.grid[i][k].y) is True) and self.grid[i][k].solid is True:
                        return True if return_tile is False else self.grid[i][k]
                if check_top is True:
                    if self.donut.coord_in_top(self.grid[i][k].x, self.grid[i][k].y) is True and self.grid[i][k].solid is True:
                        return True if return_tile is False else self.grid[i][k]
        return False if return_tile is False else None
    
    def donut_x_shift(self):
        if self.donut.x_velocity < 0: 
            if self.donut.img_x + self.donut.x_velocity > 0: #prevents donut from moving off the left side of the screen
                    self.donut.img_x += self.donut.x_velocity
                    self.donut.box_x += self.donut.x_velocity
        elif self.donut.img_x < self.donut.max_x_pos or self.grid[len(self.grid) - 1][0].on_screen(): 
            self.donut.img_x += self.donut.x_velocity
            self.donut.box_x += self.donut.x_velocity
        else:
            for i in range(len(self.grid)):
                for k in range(len(self.grid[i])):
                    self.grid[i][k].x -= self.donut.x_velocity
    
    def donut_user_imput(self):
        if self.donut_at_solid(True, False):
            if self.usable_keys[" "] is True and self.donut.active_jump is False and self.donut.frames_since_land > 2:
                self.donut.y_velocity = self.donut.jump_y_velocity
                self.donut.active_jump = True
        if (self.usable_keys[RIGHT] is True and self.usable_keys[LEFT] is True) or (self.usable_keys[RIGHT] is False and self.usable_keys[LEFT] is False):
            self.donut.x_velocity = 0
        else:
            self.donut.x_velocity = self.donut.max_x_velocity if self.usable_keys[RIGHT] is True else -1 * self.donut.max_x_velocity    
        if self.usable_keys[DOWN] is True and self.donut.active_jump is False and self.donut.frames_since_land > 2:
            if self.donut_at_solid(True, False, True) is not None and self.donut_at_solid(True, False, True).fall_through == True:
                self.donut.falling_through  = True
            
    def run_donut(self):
        self.donut_user_imput()
        if self.donut_at_solid(True, False) is False or self.donut.y_velocity < 0 or self.donut.falling_through is True:
            self.donut.jump()
        else:
            self.donut.y_velocity = 0
            self.donut.active_jump = False
        if self.donut.x_velocity != 0:
            self.donut_x_shift()
        if self.donut_at_solid(True, False) is False:
            self.donut.falling_through = False
    
    def display(self):
        while self.grid[self.tile_scroll_pos][0].on_screen() is False:
            self.tile_scroll_pos += 1
        self.run_donut()
        imageMode(CORNER)
        image(self.bkgd_img, 0,-2)
        grid_render_end = self.tile_scroll_pos + self.render_width_in_tiles if self.tile_scroll_pos + self.render_width_in_tiles < len(self.grid) else len(self.grid) - 1
        for i in range(self.tile_scroll_pos, grid_render_end):
            for k in range(len(self.grid[i])):
                self.grid[i][k].display()
                #rect(self.grid[i][k].x, self.grid[i][k].y, self.tile_size, self.tile_size)
        self.donut.display()
        
    def click(self):
        pass
