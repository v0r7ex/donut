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
        pass
        
    def reset(self):
        frameRate(30)

    def display(self):
        pass
        
        
    def click(self):
        pass
