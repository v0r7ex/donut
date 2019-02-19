from button import Button

class Menu():
    def __init__(self):
        self.load_images()
        self.create_buttons()
        self.resize_images()
        self.reset()
        
    def load_images(self):
        self.bkgd_img = loadImage("white.jpg")
        self.title_img = loadImage("menu/title.png")
        self.load_play_images()
        self.load_settings_images()
        self.load_about_images()
        self.play_word = loadImage("menu/play_word.png")
        self.settings_word = loadImage("menu/settings_word.png")
        self.about_word = loadImage("menu/about_word.png")
        
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
        self.title_img.resize(int(68 * width/100), int(9.5 * width/100))
        for i in range(24):
            self.play_frames[i].resize(self.play_button.w, self.play_button.h)
        for i in range(24):
            self.settings_frames[i].resize(self.settings_button.w, self.settings_button.h)
        for i in range(24):
            self.about_frames[i].resize(self.about_button.w, self.about_button.h)
        self.play_word.resize(self.play_button.w, self.play_button.h)
        self.settings_word.resize(self.settings_button.w, self.settings_button.h)
        self.about_word.resize(self.about_button.w, self.about_button.h)
        
    def create_buttons(self):
        self.play_button = Button(50, 70, 13, 14, self.play_frames, self.play_word)
        self.settings_button = Button(37, 75, 13, 14, self.settings_frames, self.settings_word)
        self.about_button = Button(63, 75, 13, 14, self.about_frames, self.about_word)
        
    def reset(self):
        frameRate(30)
        self.play_button.reset()
        self.settings_button.reset()
        self.about_button.reset()

    def display(self):
        imageMode(CORNER)
        image(self.bkgd_img, 0, 0)
        imageMode(CENTER)
        image(self.title_img, width/2, height/5)
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
