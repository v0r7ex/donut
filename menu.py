from simple_button import Simple_Button
from animated_button import Animated_Button

class Menu():
    def __init__(self):
        self.load_images()
        self.create_buttons()
        self.resize_images()
        
    def load_images(self):
        self.bkgd_img = loadImage("white.jpg")
        self.title_img = loadImage("title.png")
        self.load_play_images()
        self.help_img = loadImage("help.png")
        self.help_hover_img = loadImage("help_hover.png")
        self.credits_img = loadImage("credits.png")
        self.credits_hover_img = loadImage("credits_hover.png")
        
        
    def load_play_images(self):
        self.play_frames = []
        for i in range(24):
            self.play_frames.append(loadImage("menu/play_frames/play" + nf(i) + ".png"))
        
    def resize_images(self):
        self.bkgd_img.resize(width, height)
        self.title_img.resize(width/2, width/6)
        for i in range(24):
            self.play_frames[i].resize(self.play_button.w, self.play_button.h)
        self.help_img.resize(self.help_button.w, self.help_button.h)
        self.help_hover_img.resize(self.help_button.w, self.help_button.h)
        self.credits_img.resize(self.credits_button.w, self.credits_button.h)
        self.credits_hover_img.resize(self.credits_button.w, self.credits_button.h)
        
    def create_buttons(self):
        self.play_button = Animated_Button(50, 80, 25, 30, self.play_frames, 11)
        self.help_button = Simple_Button(50, 52, 24, 5, self.help_img, self.help_hover_img)        
        self.credits_button = Simple_Button(50, 64, 28, 5, self.credits_img, self.credits_hover_img)

    def display(self):
        imageMode(CORNER)
        image(self.bkgd_img, 0, 0)
        imageMode(CENTER)
        image(self.title_img, width/2, height/6)
        self.play_button.display()
        self.help_button.display()
        self.credits_button.display()
        
    def click(self):
        if self.play_button.is_hovering():
            return "game"
        elif self.help_button.is_hovering():
            return "help"
        elif self.credits_button.is_hovering():
            return "credits"
        else:
            return None
