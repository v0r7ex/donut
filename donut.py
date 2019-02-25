class Donut():
    def __init__(self):
        self.w = int(14 * width/100)
        self.h = int(14 * width/100)
        self.start_x = int(10 * width/100)
        self.start_y = int(10 * width/100)
        self.end_x = self.x + self.w
        self.end_y = self.y + self.h
        self.load_images()
        self.resize_images()
        self.state = "stand"
        self.direction = "right"
        self.current_frame = 0
        
    def load_images(self):
        self.stand_cycle_right = [loadImage("donut/circle.png"), loadImage("donut/circle.png"), loadImage("donut/circle.png")]
        self.stand_cycle_left = [loadImage("donut/circle.png"), loadImage("donut/circle.png"), loadImage("donut/circle.png")]
        self.walk_cycle_right = [loadImage("donut/circle.png"), loadImage("donut/circle.png"), loadImage("donut/circle.png")] 
        self.walk_cycle_left = [loadImage("donut/circle.png"), loadImage("donut/circle.png"), loadImage("donut/circle.png")]   
        self.jump_sequence_right = [loadImage("donut/circle.png"), loadImage("donut/circle.png"), loadImage("donut/circle.png")]
        self.jump_sequence_left = [loadImage("donut/circle.png"), loadImage("donut/circle.png"), loadImage("donut/circle.png")] 
        self.land_sequence_right = [loadImage("donut/circle.png"), loadImage("donut/circle.png"), loadImage("donut/circle.png")] 
        self.land_sequence_left = [loadImage("donut/circle.png"), loadImage("donut/circle.png"), loadImage("donut/circle.png")] 
        self.die_sequence = [loadImage("donut/circle.png"), loadImage("donut/circle.png"), loadImage("donut/circle.png")]
        
    def resize_images(self):
        for img in self.stand_cycle:
            img.resize(self.w, self.h)
        for img in self.walk_cycle:
            img.resize(self.w, self.h)
        for img in self.jump_sequence:
            img.resize(self.w, self.h)
        for img in self.land_sequence:
            img.resize(self.w, self.h)
        for img in self.die_sequence:
            img.resize(self.w, self.h)
            
    def coord_in_feet(self, x_coord, y_coord):
        return True if x_coord >= self.start_x + self.w/5 and x_coord >= self.end_x - self.w/5 and y_coord >= self.start_y + self.h * 0.9 and y_coord <= self.end_y else False
    
    def coord_in_donut(self, x_coord, y_coord):
        return True if x_coord > self.start_x and x_coord > self.end_x and y_coord > self.start_y and y_coord < self.end_y else False
            
    def iterate_cycle(self):
        if self.state = "stand":
            frame_cycle = self.stand_cycle_right if self.direction == "right" else self.stand_cycle_left
        elif self.state = "walk":
            frame_cycle = self.walk_cycle_right if self.direction == "right" else self.walk_cycle_left
        if self.current_frame < len(frame_cycle) - 1:
            self.current_frame += 1
        else:
            self.current_frame = 0
        return frame_cycle[self.current_frame]
    
    def iterate_sequence(self):
        if self.state = "jump":
            frame_sequence = self.jump_sequence_right if self.direction == "right" else self.jump_cycle_left
        elif self.state = "land":
            frame_sequence = self.lamp_sequence_right if self.direction == "right" else self.lamp_cycle_left
        elif self.state = "die":
            frame_sequence = self.die_sequence
            
    def display(self):
        imageMode(CORNER)
        img = self.iterate_cycle() if self.state == "stant" or self.state == "walk" else self.iterate_sequence()
        image(img, self.start_x, self.start_y)
        
        
