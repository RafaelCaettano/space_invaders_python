import pygame as pg
from pygame.sprite import Sprite

class Heart(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pg.transform.scale(
            pg.image.load('assets/images/heart.png'),
            (30,30)
        )                  
        self.rect = self.image.get_rect(
            center=(x,y)
        )  

    def damage(self):
        self.image = pg.transform.scale(
            pg.image.load('assets/images/black_heart.png'),
            (30,30)
        )               