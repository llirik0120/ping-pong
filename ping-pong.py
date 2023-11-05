from pygame import *


window = display.set_mode((700, 500))
display.set_caption('ping_pong')
background = (200,255,255)
window.fill(background)

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()