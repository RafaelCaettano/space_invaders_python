import pygame as pg
import os

FONTS = None

def load_all_fonts(directory, accept=('.ttf')):
    fonts = {}
    for font in os.listdir(directory):
        name,ext = os.path.splitext(font)
        if ext.lower() in accept:
            fonts[name] = os.path.join(directory, font)
    return fonts