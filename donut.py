class Donut():
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.img_width = int(11 * width/100)
        self.img_height = int(10 * width/100)
        self.img_x = int(10 * width/100)
        self.img_y = int(68 * height/100)
        self.box_x = (self.img_x + self.img_width/2) - self.tile_size #centers the 2 by 2 tile hit box relative to the img on the x-axis
        self.box_y = (self.img_y + self.img_height) - self.tile_size * 2 #aligns the hit box with the bottom of the img
        self.box_width = tile_size * 2
        self.box_height = tile_size * 2
        self.x_velocity = 0 #x velocity has infinite acceleration, except when falling in which case it slows by self.gravitational_accel
        self.max_x_velocity = self.tile_size/4 #use -1 * max_x_velocity to move left
        self.y_velocity = 0
        self.max_y_velocity = -1 * self.tile_size/4
        self.gravitational_accel = self.tile_size/100
        self.terminal_velocity = self.tile_size/3
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
            img.resize(self.img_width, self.img_height)
        for img in self.walk_cycle_right:
            img.resize(self.img_width, self.img_height)
        for img in self.jump_sequence_right:
            img.resize(self.img_width, self.img_height)
        for img in self.land_sequence_right:
            img.resize(self.img_width, self.img_height)
        for img in self.die_sequence:
            img.resize(self.img_width, self.img_height)
        for img in self.stand_cycle_left:
            img.resize(self.img_width, self.img_height)
        for img in self.walk_cycle_left:
            img.resize(self.img_width, self.img_height)
        for img in self.jump_sequence_left:
            img.resize(self.img_width, self.img_height)
        for img in self.land_sequence_left:
            img.resize(self.img_width, self.img_height)

            
    def coord_in_bottom(self, x_coord, y_coord):
        return True if x_coord >= self.box_x and x_coord >= self.box_x + self.box_width and y_coord >= self.box_y + self.box_height/2 and y_coord <= self.box_y + self.box_height else False
    
    def coord_in_top(self, x_coord, y_coord):
        return True if x_coord >= self.box_x and x_coord >= self.box_x + self.box_width and y_coord >= self.box_y and y_coord <= self.box_y + self.box_height/2 else False
            
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
            frame_sequence = self.jump_sequence_right if self.direction == "right" else self.jump_sequence_left
        elif self.state == "land":
            frame_sequence = self.lamp_sequence_right if self.direction == "right" else self.lamp_sequence_left
        elif self.state == "die":
            frame_sequence = self.die_sequence
        if self.current_frame < len(frame_sequence) - 1:
            self.current_frame += 1
        return frame_sequence[self.current_frame]
            
    def display(self):
        imageMode(CORNER)
        img = self.iterate_cycle() if self.state == "stand" or self.state == "walk" else self.iterate_sequence()
        image(img, self.img_x, self.img_y)
        
        
