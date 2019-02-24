from button import Button

class Level():
    def __init__(self, width_in_blocks, background_img):
        self.block_size = int(width/50)
        self.width_in_blocks = width_in_blocks
        self.height_in_blocks = 20
        self.grid = [[None] * self.height_in_blocks] * self.width_in_blocks
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
         
    def display(self):
        imageMode(CORNER)
        image(self.bkgd_img, 0, 0)
        for i in grid:
            for k in grid[i]:
                if grid[i][k] is not None:
                    grid[i][k].display()
        
    def click(self):
        pass
