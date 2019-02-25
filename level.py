from button import Button

class Level():
    def __init__(self, donut, width_in_blocks, background_img):
        self.donut = donut
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
        for i in range(len(self.grid)):
            for k in range(len(self.grid[i])):
                if self.grid[i][k] is not None:
                    self.grid[i][k].display()
        
    def click(self):
        pass
