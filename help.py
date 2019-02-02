from simple_button import Simple_Button

class Help():
    def __init__(self):
        self.load_images()
        self.create_buttons()
        self.resize_images()
        
    def load_images(self):
        self.bkgd_img = loadImage("white.jpg")
        self.help_img = loadImage("help.png")
        self.menu_img = loadImage("menu.png")
        self.menu_hover_img = loadImage("menu_hover.png")
        
    def resize_images(self):
        self.bkgd_img.resize(width, height)
        self.help_img.resize(int(width/2.5), width/13)
        self.menu_img.resize(self.menu_button.w, self.menu_button.h)
        self.menu_hover_img.resize(self.menu_button.w, self.menu_button.h)
        
    def create_buttons(self):
        self.menu_button = Simple_Button(50, 50, 28, 5, self.menu_img, self.menu_hover_img)

    def display(self):
        imageMode(CORNER)
        image(self.bkgd_img, 0, 0)
        imageMode(CENTER)
        image(self.help_img, width/2, height/6)
        self.menu_button.display()
        
        
    def click(self):
        if self.menu_button.is_hovering():
            return "menu"
        else:
            return None
