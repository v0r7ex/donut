from button import Button

class Game():
    def __init__(self):
        self.load_images()
        self.create_buttons()
        self.resize_images()
        self.build_level0()
        self.current_level = None
        
    def load_images(self):
        self.bkgd_img = loadImage("white.jpg")

    def resize_images(self):
        self.bkgd_img.resize(width, height)
        
    def create_buttons(self):
        pass
        
    def build_level0(self):
        self.level0 = None
        
    def reset(self):
        frameRate(30)
        self.current_level = None

    def display(self):
        self.current_level.display()
        
    def click(self): #this method will be used to interact with the pause button, etc.
        pass
