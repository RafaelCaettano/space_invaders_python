import pygame as pg
from pygame.sprite import Sprite
import settings as s
from random import randint
from tools import sprite_tools as st

class Asteroid(Sprite):
    def __init__(self):
        super().__init__()

        size = randint(40, 80)

        self.image = st.get_sprite(
            'asteroid_sprite',
            (size, size),
            randint(1, 360)
        ) 
        
        self.speed_y = 2
        self.speed_x = 2
        self.destroyed = False

        if randint(1, 2) == 1:
            direction = -1
        else:
            direction = 1

        x = 0
        y = 0

        rand = randint(1, 4)
        if rand == 1:
            y = -20
            x += randint(200, 600)
            self.speed_x = randint(0, 3) * direction
            
        elif rand == 2:
            x = -20
            y += randint(200, 400)
            self.speed_y = randint(0, 3) * direction

        elif rand == 3:
            x = s.SCREEN_WIDTH + 20
            y += randint(200, 400)
            self.speed_x *= -1
            self.speed_y = randint(0, 3) * direction

        if rand == 4:
            y = s.SCREEN_HEIGHT + 20
            x += randint(200, 400)
            self.speed_y *= -1
            self.speed_x = randint(0, 3) * direction

        self.rect = st.rect_sprite(self.image, (x, y))

    def destroy(self):
        self.destroyed = True
        self.kill()

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.y < -100 or self.rect.x < -100 or self.rect.y > s.SCREEN_HEIGHT + 100 or self.rect.x > s.SCREEN_WIDTH + 100:
            self.destroy()
