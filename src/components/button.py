import pygame as pg
from pygame.sprite import Sprite
from tools import font_tools as ft
import settings as s

class Button(Sprite):
    def __init__(self, text,  pos, size, font, color, background):
        self.x, self.y = pos
        self.w, self.h = size
        self.font = pg.font.Font(ft.FONTS[s.FONT], font)
        self.change_text(text, background, size, color)
 
    def change_text(self, text, background, size, color):
        self.text = self.font.render(text, 1, color)
        self.size = size
        self.surface = pg.Surface(self.size)
        self.surface.fill(background)
        self.surface.blit(self.text, (28, 12))
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)
        
    def click(self, pos, click):
        if self.rect.collidepoint(pos):
            if click[0]:
                return True
            return False
        return False