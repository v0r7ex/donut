class Button():
    def __init__(self, xPercent, yPercent, widthPercent, heightPercent, frames_list, hover_img):
        self.x = int(xPercent * width/100)
        self.y = int(yPercent * height/100)
        self.w = int(widthPercent * width/100)
        self.h = int(heightPercent * width/100)
        self.startX = self.x - self.w/2
        self.startY = self.y - self.h/2
        self.endX = self.x + self.w/2
        self.endY = self.y + self.h/2
        self.frames = frames_list
        self.current_frame = 0
        self.hover_img = hover_img
        self.reset()
        
    def reset(self):
        self.current_frame = 0
        
    def is_hovering(self):
        return True if mouseX > self.startX and mouseX < self.endX and mouseY > self.startY and mouseY < self.endY else False
    
    def display(self):
        if self.current_frame < (len(self.frames) - 1):
            self.current_frame += 1
        else:
            self.current_frame = 0
        imageMode(CENTER)        
        img = self.hover_img if self.is_hovering() else self.frames[self.current_frame]
        image(img, self.x, self.y)
        
