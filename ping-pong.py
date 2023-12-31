from pygame import *
font.init()

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
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
display.set_caption('ping_pong')
background = (0,79,0)
window.fill(background)

game = True
finish = False
font_1 = font.Font(None, 35)
lose1 = font_1.render('KТО ТО ЗДОХ', True, (180, 0, 0))
lose2 = font_1.render('KТО ТО ЗДОХ 2', True ,(180, 0, 0))
clock = time.Clock()
FPS = 80
speed_x = 3
speed_y = 3
racket_l = Racket (15, 80, 'platform.png', 10, 200, 10)
racket_r = Racket (15, 80, 'platform.png', 675, 200, 10)
ball = GameSprite (50, 50, 'ball.png', 325, 225, 0)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    if not finish:

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 500 - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(ball, racket_l) or sprite.collide_rect(ball, racket_r):
            speed_x *= -1



        window.fill(background)
        racket_l.update_l()
        racket_l.reset()
        racket_r.update_r()
        racket_r.reset()
        ball.reset()

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x> 650:
            finish = True
            window.blit(lose2, (200, 200))

    display.update()
    clock.tick(FPS)

