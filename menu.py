from button import Button

class Menu():
    def __init__(self):
        self.load_images()
        self.create_buttons()
        self.resize_images()
        
    def load_images(self):
        self.bkgd_img = loadImage("white.jpg")
        self.play_img = loadImage("play.png")
        self.play_hover_img = loadImage("play_hover.png")
        
        
    def resize_images(self):
        self.bkgd.resize(width, height)
        self.play_img.resize(self.play_button.w, self.play_button.h)
        self.play_hover_img.resize(self.play_button.w, self.play_button.h)
        
    def create_buttons(self):
        self.play_button = Button(50, 30, 15, 8, self.play_img, self.play_hover_img)
        
    def display(self):
        imageMode(CORNER)
        image(self.bkgd, 0, 0)
        
    def click(self):
        pass
