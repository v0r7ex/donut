class Tile():
    def __init__(self, x, y, tile_size, img, solid, fall_through):
        self.x = x
        self.y = y
        self.tile_size = tile_size
        self.update_end_coords()
        self.img = img
        self.solid = solid
        self.fall_through = fall_through
        
    def update_end_coords(self):
        self.end_x = self.x + self.tile_size
        self.end_y = self.y + self.tile_size
    
    def check_hit(self, test_x, test_y,):
        self.update_end_coords()
        return True if self.x <= test_x and test_x <= self.end_x and self.y <= test_y and test_y <= self.end_y else False
    
    def on_screen(self):
        return True if self.x > 0 - self.tile_size and self.x < width else False
    
    def display(self):
        if self.img is not None and self.on_screen():
            imageMode(CORNER)
            image(self.img, self.x, self.y)
   
