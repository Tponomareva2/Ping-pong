from pygame import*
from random import randint

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('пинг понг')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

racket = Player('racket1.png', 100, 400, 5)
racket2 = Player('racket2.png', 500, 400, 5)
ball = GameSprite('ping.png', 100, 200, 5)
speed_x = 3
speed_y = 3

clock = time.Clock()
FPS = 60
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide_rect(racket, ball) or  sprite.collide_rect(racket2, ball):
        speed_x *= -1
    
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    
    window.blit(background,(0,0))
    clock.tick(FPS)
    racket.update_l()
    racket.reset()
    racket2.update_r()
    racket2.reset()
    ball.reset()
   
    
    display.update()
