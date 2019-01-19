from button import Button

class Menu():
    def __init__(self):
        self.load_images()
        self.create_buttons()
        self.resize_images()
        
    def load_images(self):
        self.bkgd_img = loadImage("white.jpg")
        self.title_img = loadImage("title.png")
        self.play_img = loadImage("play.png")
        self.play_hover_img = loadImage("play_hover.png")
        self.help_img = loadImage("help.png")
        self.help_hover_img = loadImage("help_hover.png")
        self.credits_img = loadImage("credits.png")
        self.credits_hover_img = loadImage("credits_hover.png")
        
    def resize_images(self):
        self.bkgd_img.resize(width, height)
        self.title_img.resize(width/2, width/6)
        self.play_img.resize(self.play_button.w, self.play_button.h)
        self.play_hover_img.resize(self.play_button.w, self.play_button.h)
        self.help_img.resize(self.help_button.w, self.help_button.h)
        self.help_hover_img.resize(self.help_button.w, self.help_button.h)
        self.credits_img.resize(self.credits_button.w, self.credits_button.h)
        self.credits_hover_img.resize(self.credits_button.w, self.credits_button.h)
        
    def create_buttons(self):
        self.play_button = Button(50, 40, 24, 5, self.play_img, self.play_hover_img)
        self.help_button = Button(50, 52, 24, 5, self.help_img, self.help_hover_img)        
        self.credits_button = Button(50, 64, 28, 5, self.credits_img, self.credits_hover_img)

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
