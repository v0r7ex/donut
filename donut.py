class Donut():
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.img_width = int(2.5 * self.tile_size)
        self.img_height = int(0.9 * self.img_width)
        self.img_x = width/10
        self.img_y = 0
        self.box_x = (self.img_x + self.img_width/2) - self.tile_size/2
        self.box_y = int(self.img_y + 0.15 * self.img_height)
        self.box_width = self.tile_size
        self.box_height = int(0.85 * self.img_height)
        self.x_velocity = 0 #x_velocity has infinite acceleration
        self.max_x_velocity = self.tile_size/4 #use -1 * max_x_velocity to move left
        self.max_x_pos = width/7
        self.y_velocity = 0
        self.jump_y_velocity = -1 * self.tile_size/1.7
        self.gravitational_accel = 3 * floor(self.tile_size/40) 
        self.terminal_velocity = self.gravitational_accel * 5
        self.load_images()
        self.resize_images()
        self.state = "stand"
        self.direction = "right"
        self.active_jump = False
        self.frames_since_land = 0
        self.falling_through = False
        self.current_frame = 0
        self.dead = False
        self.coma_frames = 0
        
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
        self.win_sequence = [loadImage("donut/stand/stand_right1.png")]
        
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
        for img in self.win_sequence:
            img.resize(self.img_width, self.img_height)

            
    def coord_in_bottom(self, x_coord, y_coord):
        return True if x_coord >= self.box_x and x_coord <= self.box_x + self.box_width and y_coord >= self.box_y + 0.75 * self.box_height and y_coord <= self.box_y + self.box_height else False
    
    def coord_in_top(self, x_coord, y_coord):
        return True if x_coord >= self.box_x and x_coord <= self.box_x + self.box_width and y_coord >= self.box_y and y_coord <= self.box_y + self.box_height/2 else False
    
    def jump(self):
        if self.y_velocity < self.terminal_velocity:
            self.y_velocity += self.gravitational_accel
        self.img_y += self.y_velocity
        self.box_y += self.y_velocity
            
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
        elif self.state == "win":
            frame_sequence = self.win_sequence
        if self.current_frame < len(frame_sequence) - 1:
            self.current_frame += 1
        return frame_sequence[self.current_frame]
            
    def display(self):
        if self.y_velocity != 0:
            if self.state is not "jump":
                self.current_frame = 0
            self.state = "jump"
        elif self.x_velocity == 0:
            self.state = "stand"
        else:
            self.state = "walk"
        if self.x_velocity != 0:
            self.direction = "right" if self.x_velocity > 0 else "left"
        if self.active_jump is False:
            self.frames_since_land += 1
        else:
            self.frames_since_land = 0
        imageMode(CORNER)
        img = self.iterate_cycle() if self.state == "stand" or self.state == "walk" else self.iterate_sequence()
        image(img, self.img_x, self.img_y)
        #rect(self.box_x, self.box_y, self.box_width, self.box_height) #shows hit box
        
    def display_without_running(self):
        imageMode(CORNER)
        img = self.iterate_cycle() if self.state == "stand" or self.state == "walk" else self.iterate_sequence()
        image(img, self.img_x, self.img_y)
        
        
