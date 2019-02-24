from button import Button

class Settings():
        def __init__(self):
        self.load_images()
        self.create_buttons()
        self.resize_images()
        
    def load_images(self):
        self.bkgd_img = loadImage("white.jpg")

    def resize_images(self):
        self.bkgd_img.resize(width, height)
        
    def create_buttons(self):
        pass
        
    def reset(self):
        frameRate(30)

    def display(self):
        imageMode(CORNER)
        image(self.bkgd_img, 0, 0)
        
    def click(self):
        pass
