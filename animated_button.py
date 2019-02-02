class Animated_Button():
    def __init__(self, xPercent, yPercent, widthPercent, heightPercent, frame_dict, hover_frame_num, visible = True):
        self.x = int(xPercent * width/100)
        self.y = int(yPercent * height/100)
        self.w = int(widthPercent * width/100)
        self.h = int(heightPercent * width/100)
        self.startX = self.x - self.w/2
        self.startY = self.y - self.h/2
        self.endX = self.x + self.w/2
        self.endY = self.y + self.h/2
        self.frame_dict = frame_dict
        self.hover_frame = self.frame_dict[hover_frame_num]
        self.visible = visible
        
    def is_hovering(self):
        return True if mouseX > self.startX and mouseX < self.endX and mouseY > self.startY and mouseY < self.endY else False
    
    def display(self):
        if self.visible:
            imageMode(CENTER)
            if self.is_hovering():
                image(self.hover_img, self.x, self.y)
            else:
                image(self.main_img, self.x, self.y)
