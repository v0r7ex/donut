add_library("minim")
from program import Program

def setup():
    fullScreen(1) #optimize for 1920 by 1080
    frameRate(30)
    global program_instance
    global usable_keys
    usable_keys = {
                    UP: False,
                    DOWN: False,
                    RIGHT: False,
                    LEFT: False,
                    " ":  False
                    }
    program_instance = Program(usable_keys)
    minim = Minim(this)
    program_instance.menu_soundtrack = minim.loadFile("audio/smile_bensound.mp3")
    program_instance.game_soundtrack = minim.loadFile("audio/happy_life_fredji.mp3")
    program_instance.current_soundtrack = program_instance.menu_soundtrack
    program_instance.menu_soundtrack.loop()
    noFill()
   
def draw():
    global program_instance
    background(50)
    program_instance.display()

def mousePressed():
    global program_instance
    program_instance.click()
    
def keyPressed():
    global usable_keys
    key_index = keyCode if key == CODED else key
    if key_index in usable_keys and usable_keys[key_index] is False:
        usable_keys[key_index] = True
        
def keyReleased():
    global usable_keys
    key_index = keyCode if key == CODED else key
    if key_index in usable_keys and usable_keys[key_index] is True:
        usable_keys[key_index] = False
