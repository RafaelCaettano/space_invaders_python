import pygame as pg
from pygame.sprite import Sprite
import settings as s
from random import randint

class Asteroid(Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.transform.scale(
            pg.image.load('assets/images/asteroid_sprite.png'),
            (30,30)
        )           
        self.speed_y = 0
        self.speed_x = 0

        rand = randint(1, 4)

        if randint(1, 2) == 1:
            direction = -1
        else:
            direction = 1

        x = 0
        y = 0
        if rand == 1:
            y = 0
            x += randint(0, s.SCREEN_WIDTH)
            self.speed_y = 7
            self.speed_x = randint(0, 7) * direction
        elif rand == 2:
            x = 0
            y += randint(0, s.SCREEN_HEIGHT)
            self.speed_x = 7
            self.speed_y = randint(0, 7) * direction
        elif rand == 3:
            x = s.SCREEN_WIDTH
            y += randint(0, s.SCREEN_HEIGHT)
            self.speed_x = -7
            self.speed_y = randint(0, 7) * direction
        if rand == 4:
            y = s.SCREEN_HEIGHT
            x += randint(0, s.SCREEN_WIDTH)
            self.speed_y = -7
            self.speed_x = randint(0, 7) * direction

        self.rect = self.image.get_rect(
            center=(x,y)
        )  

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y < 0 or self.rect.x < 0:
            self.kill()
