import pygame as pg
from pygame.sprite import Sprite
from tools import sprite_tools as st

class Shield(Sprite):
    def __init__(self, pos):
        super().__init__()

        self.x, self.y = pos
        self.image = st.get_sprite(
            'shield_sprite',
            (88.88, 44.44)
        )
        self.rect = st.rect_sprite(self.image, pos)
        self.counters()

    def counters(self):
        self.lives = 5
    
    def damage(self):
        self.lives -= 1
        if self.lives == 3:
            self.image = st.get_sprite(
                'shield_3_sprite',
                (75, 50)
            )
            self.rect = st.rect_sprite(self.image, (self.x + 5, self.y))

        if self.lives == 1:
            self.image = st.get_sprite(
                'shield_2_sprite',
                (65, 25)
            )
            self.rect = st.rect_sprite(self.image, (self.x + 15, self.y))
        
        if self.lives == 0:
            self.kill() 