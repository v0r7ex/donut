from button import Button
from tile import Tile

class Level():
    def __init__(self, donut, tile_size, width_in_tiles, background_img):
        self.donut = donut
        self.tile_size = tile_size
        self.width_in_tiles = width_in_tiles
        self.height_in_tiles = 20
        self.grid = [[None] * self.height_in_tiles] * self.width_in_tiles
        self.populate_grid()
        self.bkgd_img = background_img
        self.load_images()
        self.create_buttons()
        self.resize_images()
        
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
                #print self.grid[i][k].x
        print self.grid[2][4].x
                
    def build_platform(self, i_coord, k_coord, length_in_tiles, img, solid = True):
        for i in range(i_coord, i_coord + length_in_tiles + 1):
            self.grid[i][k_coord].img = img
            self.grid[i][k_coord].solid = solid
                
    def display(self):
        imageMode(CORNER)
        image(self.bkgd_img, 0, 0)
        for i in range(len(self.grid)):
            for k in range(len(self.grid[i])):
                self.grid[i][k].display()
        self.donut.display()
        
    def click(self):
        pass
