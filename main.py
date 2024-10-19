import random

import pgzrun
import pygame

pygame.mouse.set_visible(False)

WIDTH = 720
HEIGHT = 480

target1 = Actor('target_red1')
target2 = Actor('target_colored')
target3 = Actor('duck_yellow')
crosshair = Actor('crosshair_white_large')
target1.y = 300

score = 0


def update():
    target1.x += 3
    target2.x += 5
    target3.x += 7
    if target1.left > WIDTH:
        target1.right = 0
        target1.top = random.randint(0, HEIGHT - target1.height)
    if target2.left > WIDTH:
        target2.right = 0
        target2.top = random.randint(0, HEIGHT - target2.height)
    if target3.left > WIDTH:
        target3.right = 0
        target3.top = random.randint(0, HEIGHT - target3.height)


def on_mouse_move(pos):
    # print(pos)
    crosshair.pos = pos


def on_mouse_down(pos):
    global score
    if crosshair.colliderect(target1):
        # print('target1')
        score += 10
        target1.right = 0
        target1.top = random.randint(0, HEIGHT - target1.height)
    elif crosshair.colliderect(target2):
        # print('target2')
        score += 10
        target2.right = 0
        target2.top = random.randint(0, HEIGHT - target2.height)
    elif crosshair.colliderect(target3):
        # print('duck')
        score -= 50
        target3.right = 0
        target3.top = random.randint(0, HEIGHT - target3.height)


def draw():
    screen.clear()
    target1.draw()
    target2.draw()
    target3.draw()
    crosshair.draw()
    screen.draw.text(str(score), (10, 10), fontsize=70)


pgzrun.go()
