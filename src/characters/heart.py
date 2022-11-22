import pygame as pg
from pygame.sprite import Sprite
from tools import sprite_tools as st

class Heart(Sprite):
    def __init__(self, position):
        super().__init__()
        
        self.image = st.get_sprite(
            'heart',
            (30,30)
        ) 
        self.rect = st.rect_sprite(self.image, position)

    def damage(self):
        self.image = st.get_sprite(
            'black_heart',
            (30,30)
        )           