from control import Control
from tools import sprite_tools as st
from tools import font_tools as ft
import pygame as pg
import settings as s

pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(s.ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(s.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()  

ft.FONTS = ft.load_all_fonts('src/assets/fonts')
st.GFX = st.load_all_gfx('src/assets/images')

control = Control()
control.main()

