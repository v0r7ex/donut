
add_library("minim")
from program import Program

def setup():
    fullScreen(2) #optimize for 1920 by 1080
    global program_instance
    program_instance = Program()
    minim = Minim(this)
    program_instance.menu_soundtrack = minim.loadFile("menu/smile_bensound.mp3")
    program_instance.game_soundtrack = minim.loadFile("game/happy_life_fredji.mp3")
    program_instance.current_soundtrack = program_instance.menu_soundtrack
    program_instance.menu_soundtrack.loop()
    global usable_keys = {
                          "UP": False
                          "DOWN": False
                          "RIGHT": False
                          "LEFT": False
                          "
                          }
    
    
def draw():
    global program_instance
    background(50)
    program_instance.display()

    
def mousePressed():
    global program_instance
    program_instance.click()
    
