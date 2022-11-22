import pygame as pg

# Medidas da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)
ORIGINAL_CAPTION = 'Space Invaders'
FPS = 120

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonte Padrão
FONT = 'ChakraPetchBold'

controls = {
    pg.K_UP: {
        'shoot_speed': (0, -7),
        'image_rotate': 0,
        'shoot_direction': 90
    },
    pg.K_RIGHT: {
        'shoot_speed': (7, 0),
        'image_rotate': 270,
        'shoot_direction': 0
    },
    pg.K_DOWN: {
        'shoot_speed': (0, 7),
        'image_rotate': 180,
        'shoot_direction': 270
    },
    pg.K_LEFT: {
        'shoot_speed': (-7, 0),
        'image_rotate': 90,
        'shoot_direction': 180
    }
}