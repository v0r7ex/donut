add_library("minim")
from program import Program

def setup():
    size(1920, 1080)
    global program_instance
    program_instance = Program()
    minim = Minim(this)
    program_instance.menu_soundtrack = minim.loadFile("menu/smile.mp3")
    program_instance.menu_soundtrack.play()
    
    
def draw():
    global program_instance
    background(50)
    program_instance.display()
    
def mousePressed():
    global program_instance
    program_instance.click()
