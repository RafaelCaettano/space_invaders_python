import pygame as pg
import os

GFX = None

def load_all_gfx(directory, color_key=(255, 0, 255), accept=('.png', '.jpg', '.bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(color_key)
            graphics[name]=img
    return graphics

def get_sprite(sprite_name, size, rotate=0):
    sprite = None

    sprite = pg.transform.scale(
        GFX[sprite_name],
        size
    )         
    sprite = pg.transform.rotate(sprite, rotate)

    return sprite

# def rect_sprite(sprite, rect):
#     x, y = rect
#     return pg.Rect(x, y, 15, 35)
    

def rect_sprite(sprite, rect):
    return sprite.get_rect(
        center=(rect)
    )

def rotate_sprite(sprite, rotate):
    return pg.transform.rotate(sprite, rotate)
