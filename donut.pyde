from program import Program

def setup():
    size(1920, 1080)
    global program_instance
    program_instance = Program()
    
    
def draw():
    global program_instance
    background(50)
    program_instance.display()

    
def mousePressed():
    global program_instance
    program_instance.click()
