import pgzrun

WIDTH = 720
HEIGHT = 480

target1 = Actor('target_red1')

def update():
    target1.x += 1

def draw():
    screen.clear()
    target1.draw()

pgzrun.go()