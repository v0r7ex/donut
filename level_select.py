from button import Button

class Level_Select():
    def __init__(self):
        self.load_images()
        self.create_buttons()
        self.resize_images()
        
    def load_images(self):
        self.bkgd_img = loadImage("white.jpg")
        self.img0 = [loadImage("level_select/level_icon0.png")]
        self.img1 = [loadImage("level_select/level_icon1.png")]
        self.img2 = [loadImage("level_select/level_icon2.png")]
        self.img3 = [loadImage("level_select/level_icon3.png")]
        self.img4 = [loadImage("level_select/level_icon4.png")]
        self.img5 = [loadImage("level_select/level_icon5.png")]
        self.img6 = [loadImage("level_select/level_icon6.png")]
        self.img7 = [loadImage("level_select/level_icon7.png")]
        self.img8 = [loadImage("level_select/level_icon8.png")]
        self.img9 = [loadImage("level_select/level_icon9.png")]
        
    def resize_images(self):
        self.bkgd_img.resize(width, height)
        self.img0[0].resize(self.level_button0.w, self.level_button0.h)
        self.img1[0].resize(self.level_button1.w, self.level_button1.h)
        self.img2[0].resize(self.level_button2.w, self.level_button2.h)
        self.img3[0].resize(self.level_button3.w, self.level_button3.h)
        self.img4[0].resize(self.level_button4.w, self.level_button4.h)
        self.img5[0].resize(self.level_button5.w, self.level_button5.h)
        self.img6[0].resize(self.level_button6.w, self.level_button6.h)
        self.img7[0].resize(self.level_button7.w, self.level_button7.h)
        self.img8[0].resize(self.level_button8.w, self.level_button8.h)
        self.img9[0].resize(self.level_button9.w, self.level_button9.h)
    
    def create_buttons(self):
        self.level_button0 = Button(30, 50, 8, 8, self.img0, self.img0[0])
        self.level_button1 = Button(40, 50, 8, 8, self.img1, self.img1[0])
        self.level_button2 = Button(50, 50, 8, 8, self.img2, self.img2[0])
        self.level_button3 = Button(60, 50, 8, 8, self.img3, self.img3[0])
        self.level_button4 = Button(70, 50, 8, 8, self.img4, self.img4[0])
        self.level_button5 = Button(30, 72, 8, 8, self.img5, self.img5[0])
        self.level_button6 = Button(40, 72, 8, 8, self.img6, self.img6[0])
        self.level_button7 = Button(50, 72, 8, 8, self.img7, self.img7[0])
        self.level_button8 = Button(60, 72, 8, 8, self.img8, self.img8[0])
        self.level_button9 = Button(70, 72, 8, 8, self.img9, self.img9[0])
        
    def reset(self):
        pass
        
    def display(self):
        imageMode(CORNER)
        image(self.bkgd_img, 0, 0)
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
        if self.level_button0.is_hovering():
            return "level0"
