from button import Button

class Level_Select():
    def __init__(self):
        self.load_images()
        self.create_buttons()
        self.resize_images()
        
    def load_images(self):
        self.img0 = [loadImage("/level/level_icon0.png")]
        self.img1 = [loadImage("/level/level_icon1.png")]
        self.img2 = [loadImage("/level/level_icon2.png")]
        self.img3 = [loadImage("/level/level_icon3.png")]
        self.img4 = [loadImage("/level/level_icon4.png")]
        self.img5 = [loadImage("/level/level_icon5.png")]
        self.img6 = [loadImage("/level/level_icon6.png")]
        self.img7 = [loadImage("/level/level_icon7.png")]
        self.img8 = [loadImage("/level/level_icon8.png")]
        self.img9 = [loadImage("/level/level_icon9.png")]
        
    def resize_images(self):
        self.img0.resize(self.img0.w, self.img0.h)
        self.img1.resize(self.img1.w, self.img1.h)
        self.img2.resize(self.img2.w, self.img2.h)
        self.img3.resize(self.img3.w, self.img3.h)
        self.img4.resize(self.img4.w, self.img4.h)
        self.img5.resize(self.img5.w, self.img5.h)
        self.img6.resize(self.img6.w, self.img6.h)
        self.img7.resize(self.img7.w, self.img7.h)
        self.img8.resize(self.img8.w, self.img8.h)
        self.img9.resize(self.img9.w, self.img9.h)
    
    def create_buttons(self):
        self.level_button0 = Button(30, 35, 5, 5, self.img0, 0)
        self.level_button1 = Button(35, 35, 5, 5, self.img1, 0)
        self.level_button2 = Button(40, 35, 5, 5, self.img2, 0)
        self.level_button3 = Button(45, 35, 5, 5, self.img3, 0)
        self.level_button4 = Button(50, 35, 5, 5, self.img4, 0)
        self.level_button5 = Button(55, 35, 5, 5, self.img5, 0)
        self.level_button6 = Button(60, 35, 5, 5, self.img6, 0)
        self.level_button7 = Button(65, 35, 5, 5, self.img7, 0)
        self.level_button8 = Button(70, 35, 5, 5, self.img8, 0)
        self.level_button9 = Button(75, 35, 5, 5, self.img9, 0)
        
    def display(self):
        self.level_button0.display()
        self.level_button1.display()
        self.level_button2.display()
        self.level_button3.display()
        self.level_button4.display()
        self.level_button5.display()
        self.level_button6.display()
        self.level_button7.display()
        self.level_button8.display()
        self.level_button9.display()
        
    def click(self):
        pass
