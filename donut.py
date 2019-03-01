class Donut():
    def __init__(self):
        self.w = int(11 * width/100)
        self.h = int(10 * width/100)
        self.start_x = int(10 * width/100)
        self.start_y = int(68 * height/100)
        self.end_x = self.start_x + self.w
        self.end_y = self.start_y + self.h
        self.load_images()
        self.resize_images()
        self.state = "stand"
        self.direction = "right"
        self.current_frame = 0
        
    def load_images(self):
        self.stand_cycle_right = [loadImage("donut/stand/stand_right1.png")]
        self.stand_cycle_left = [loadImage("donut/stand/stand_left1.png")]
        self.walk_cycle_right = []
        self.walk_cycle_left = []
        for i in range(1, 16):
            self.walk_cycle_right.append(loadImage("donut/walk/walk_right" + nf(i) + ".png"))
            self.walk_cycle_left.append(loadImage("donut/walk/walk_left" + nf(i) + ".png"))
        self.jump_sequence_right = [loadImage("donut/jump/jump_right1.png")]
        self.jump_sequence_left = [loadImage("donut/jump/jump_left1.png")] 
        self.land_sequence_right = [loadImage("donut/stand/stand_right1.png")] 
        self.land_sequence_left = [loadImage("donut/stand/stand_left1.png")] 
        self.die_sequence = [loadImage("donut/stand/stand_right1.png")]
        
    def resize_images(self):
        for img in self.stand_cycle_right:
            img.resize(self.w, self.h)
        for img in self.walk_cycle_right:
            img.resize(self.w, self.h)
        for img in self.jump_sequence_right:
            img.resize(self.w, self.h)
        for img in self.land_sequence_right:
            img.resize(self.w, self.h)
        for img in self.die_sequence:
            img.resize(self.w, self.h)
        for img in self.stand_cycle_left:
            img.resize(self.w, self.h)
        for img in self.walk_cycle_left:
            img.resize(self.w, self.h)
        for img in self.jump_sequence_left:
            img.resize(self.w, self.h)
        for img in self.land_sequence_left:
            img.resize(self.w, self.h)

            
    def coord_in_feet(self, x_coord, y_coord):
        return True if x_coord >= self.start_x + self.w/5 and x_coord >= self.end_x - self.w/5 and y_coord >= self.start_y + self.h * 0.9 and y_coord <= self.end_y else False
    
    def coord_in_donut(self, x_coord, y_coord):
        return True if x_coord > self.start_x and x_coord > self.end_x and y_coord > self.start_y and y_coord < self.end_y else False
            
    def iterate_cycle(self):
        if self.state == "stand":
            frame_cycle = self.stand_cycle_right if self.direction == "right" else self.stand_cycle_left
        elif self.state == "walk":
            frame_cycle = self.walk_cycle_right if self.direction == "right" else self.walk_cycle_left
        if self.current_frame < len(frame_cycle) - 1:
            self.current_frame += 1
        else:
            self.current_frame = 0
        return frame_cycle[self.current_frame]
    
    def iterate_sequence(self):
        if self.state == "jump":
            frame_sequence = self.jump_sequence_right if self.direction == "right" else self.jump_cycle_left
        elif self.state == "land":
            frame_sequence = self.lamp_sequence_right if self.direction == "right" else self.lamp_cycle_left
        elif self.state == "die":
            frame_sequence = self.die_sequence
        if self.current_frame < len(frame_sequence) - 1:
            self.current_frame += 1
        return frame_sequence[self.current_frame]
            
    def display(self):
        imageMode(CORNER)
        img = self.iterate_cycle() if self.state == "stand" or self.state == "walk" else self.iterate_sequence()
        image(img, self.start_x, self.start_y)
        
        
