from button import Button
from tile import Tile

class Level():
    def __init__(self, donut, tile_size, width_in_tiles, background_img):
        self.donut = donut
        self.tile_size = tile_size
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
                self.grid[i][k] = Tile(i * self.tile_size, k * self.tile_size, self.tile_size, None, False)
                
    def build_platform(self, i_coord, k_coord, length_in_tiles, img, solid = True):
        for i in range(i_coord, i_coord + length_in_tiles + 1):
            self.grid[i][k_coord].img = img
            self.grid[i][k_coord].solid = solid
            
    def donut_at_solid(self, check_bottom = True, check_top = True):
        for i in range(self.tile_scroll_pos, self.tile_scroll_pos + self.render_width_in_tiles):
            for k in range(len(self.grid[i])):
                if check_bottom is True:
                    if self.donut.coord_in_bottom(self.grid[i][k].x, self.grid[i][k].y) is True:
                        return True
                if check_top is True:
                    if self.donut.coord_in_top(self.grid[i][k].x, self.grid[i][k].y) is True:
                        return True
        return False
    
    def run_donut(self):
        if self.donut_at_solid(True, False) is False:
            self.donut.fall()
                
    def display(self):
        while self.grid[self.tile_scroll_pos][0].on_screen() is False:
            self.tile_scroll_pos += 1
        self.run_donut()
        imageMode(CORNER)
        image(self.bkgd_img, 0,-2)
        for i in range(self.tile_scroll_pos, self.tile_scroll_pos + self.render_width_in_tiles):
            for k in range(len(self.grid[i])):
                self.grid[i][k].display()
        self.donut.display()
        
    def click(self):
        pass
