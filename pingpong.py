from pygame import*
from random import randint

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
game = True

while game:
    window.blit(background,(0,0))
    
 
    display.update()