import pygame as pg
from pygame.sprite import Sprite
import settings as s
from random import randint

class Asteroid(Sprite):
    def __init__(self):
        super().__init__()

        size = randint(40, 80)
        self.image = pg.transform.scale(
            pg.image.load('assets/images/asteroid_sprite.png'),
            (size,size)
        )           
        self.image = pg.transform.rotate(self.image, randint(1, 360))

        self.speed_y = 3
        self.speed_x = 3
        self.destroyed = False

        rand = randint(1, 4)

        if randint(1, 2) == 1:
            direction = -1
        else:
            direction = 1

        x = 0
        y = 0
        if rand == 1:
            y = 0
            x += randint(200, 600)
            self.speed_x = randint(0, 3) * direction
            
        elif rand == 2:
            x = 0
            y += randint(200, 400)
            self.speed_y = randint(0, 3) * direction

        elif rand == 3:
            x = s.SCREEN_WIDTH
            y += randint(200, 400)
            self.speed_x *= -1
            self.speed_y = randint(0, 3) * direction

        if rand == 4:
            y = s.SCREEN_HEIGHT
            x += randint(200, 400)
            self.speed_y *= -1
            self.speed_x = randint(0, 3) * direction

        self.rect = self.image.get_rect(
            center=(x,y)
        )  

    def destroy(self):
        self.destroyed = True
        self.kill()


    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.y < -45 or self.rect.x < -45:
            self.destroy()

