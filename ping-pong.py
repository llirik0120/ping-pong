from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, size_x, size_y, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Racket(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_1(self):
        keys = key

window = display.set_mode((700, 500))
display.set_caption('ping_pong')
background = (200,255,255)
window.fill(background)

game = True

racket1 = () 
racket2 =

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()

