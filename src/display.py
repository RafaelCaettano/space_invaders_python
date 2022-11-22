import pygame as pg
import settings as s
from tools import sprite_tools as st

class Display():

    def set_display(self):
        self.screen = pg.display.set_mode(s.SCREEN_SIZE, pg.RESIZABLE)

        self.background = st.get_sprite(
            'background',
            s.SCREEN_SIZE
        ) 
    
    def blit_display(self):
        self.screen.blit(
            self.background, 
            (0, 0)
        )  

    def blit_text(self, label):
        self.screen.blit(
            label.text, 
            label.rect
        )

    def blit_button(self, button):
        self.screen.blit(
            button.surface, 
            button.rect
        )

    def set_fps(self):
        clock = pg.time.Clock()
        clock.tick(s.FPS)