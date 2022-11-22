import pygame as pg
import settings as s
from tools import font_tools as ft

class Label():
    def __init__(self, text, fs, pos, color):
        self.text = None
        self.rect = None
        self.create_label(text, fs, pos, color)

    def create_label(self, text, fs, pos, color):
        font = pg.font.Font(ft.FONTS[s.FONT], fs)
        self.text = font.render(text, True, color)
        self.rect = self.text.get_rect()
        self.rect.center = (pos)

