import pygame as pg
from pygame.sprite import Sprite

class Shield(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
        self.image = pg.transform.scale(
            pg.image.load('assets/images/shield_sprite.png'),
            (88.88,44.44)
        )            
        self.rect = self.image.get_rect(
            center=(x,y)
        )
        self.counters()

    def counters(self):
        self.lives = 5
    
    def damage(self):
        self.lives -= 1
        if self.lives == 3:
            self.image = pg.transform.scale(
                pg.image.load('assets/images/shield_3_sprite.png'),
                (75,50)
            )   
            self.rect = self.image.get_rect(
                center=(self.x + 5, self.y)
            )

        if self.lives == 1:
            self.image = pg.transform.scale(
                pg.image.load('assets/images/shield_2_sprite.png'),
                (65,25)
            )   
            self.rect = self.image.get_rect(
                center=(self.x + 15, self.y)
            )
        
        if self.lives == 0:
            self.kill() 