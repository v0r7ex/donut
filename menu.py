from simple_button import Simple_Button
from animated_button import Animated_Button

class Menu():
    def __init__(self):
        self.load_images()
        self.create_buttons()
        self.resize_images()
        self.reset()
        
    def load_images(self):
        self.bkgd_img = loadImage("white.jpg")
        self.title_img = loadImage("title.png")
        self.load_play_images()
        self.load_settings_images()
        self.load_about_images()
        
    def load_play_images(self):
        self.play_frames = []
        for i in range(24):
            self.play_frames.append(loadImage("menu/play_frames/play" + nf(i) + ".png"))
            
    def load_settings_images(self):
        self.settings_frames = []
        for i in range(24):
            self.settings_frames.append(loadImage("menu/settings_frames/settings" + nf(i) + ".png"))
            
    def load_about_images(self):
        self.about_frames = []
        for i in range(24):
            self.about_frames.append(loadImage("menu/about_frames/about" + nf(i) + ".png"))
        
    def resize_images(self):
        self.bkgd_img.resize(width, height)
        self.title_img.resize(width/2, width/6)
        for i in range(24):
            self.play_frames[i].resize(self.play_button.w, self.play_button.h)
        for i in range(24):
            self.settings_frames[i].resize(self.settings_button.w, self.settings_button.h)
        for i in range(24):
            self.about_frames[i].resize(self.about_button.w, self.about_button.h)
        
    def create_buttons(self):
        self.play_button = Animated_Button(50, 70, 13, 14, self.play_frames, 11)
        self.settings_button = Animated_Button(37, 75, 13, 14, self.settings_frames, 11)
        self.about_button = Animated_Button(63, 75, 13, 14, self.about_frames, 11)
        
    def reset(self):
        frameRate(30)
        self.play_button.reset()

    def display(self):
        imageMode(CORNER)
        image(self.bkgd_img, 0, 0)
        imageMode(CENTER)
        #image(self.title_img, width/2, height/6)
        self.play_button.display()
        self.settings_button.display()
        self.about_button.display()
        
    def click(self):
        if self.play_button.is_hovering():
            return "game"
        elif self.settings_button.is_hovering():
            return "settings"
        elif self.about_button.is_hovering():
            return "about"
        else:
            return None
