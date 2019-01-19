from button import Button

class Menu():
    def __init__(self):
        self.load_images()
        self.resize_images()
        
    def load_images(self):
        self.bkgd = loadImage("white.jpg")
        
    def resize_images(self):
        self.bkgd.resize(width, height)
        
    def create_buttons(self):
        pass
        
    def display(self):
        imageMode(CORNER)
        image(self.bkgd, 0, 0)
        
    def click(self):
        pass
