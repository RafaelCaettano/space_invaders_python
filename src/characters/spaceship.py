import pygame as pg
from pygame.sprite import Sprite
from pygame.locals import QUIT
import settings as s
import time
from tools import sprite_tools as st

class Spaceship(Sprite):
    def __init__(self, shoots):
        super().__init__()

        image = st.get_sprite(
            'spaceship_sprite',
            (55, 70)
        ) 
        self.image = image
        self.aux_image = image
        self.rect = st.rect_sprite(self.image, (400, 520))
        
        self.counters()
        self.physics()
        self.set_direction(pg.K_UP)
        
        self.shoots = shoots
        self.inicial_shoot_timer = time.time()
    
    def counters(self):
        self.lives = 3
        self.shoots_counter = 0

    def physics(self):
        self.speed = 3
        self.shoot_speed = (0, 0)

    def damage(self):
        self.lives -= 1

    def move(self, free):
        keys = pg.key.get_pressed()
        if free:
            if keys[pg.K_LEFT] and self.rect.x > 0:
                self.rect.x -= self.speed
                self.set_direction(pg.K_LEFT)

            if keys[pg.K_RIGHT] and self.rect.x < 745:
                self.rect.x += self.speed
                self.set_direction(pg.K_RIGHT)

            if keys[pg.K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
                self.set_direction(pg.K_UP)

            if keys[pg.K_DOWN] and self.rect.y < 550:
                self.rect.y += self.speed
                self.set_direction(pg.K_DOWN)
        else:
            if keys[pg.K_LEFT] and self.rect.x > 0:
                self.rect.x -= self.speed
            if keys[pg.K_RIGHT] and self.rect.x < 745:
                self.rect.x += self.speed
                
            self.set_direction(pg.K_UP)
    
    def actions(self, free):
        self.move(free)
        for event in pg.event.get():  
            if event.type == QUIT:
                pg.quit()
            
            current_timer = time.time()
            current_time = round(
                current_timer - self.inicial_shoot_timer, 
                1
            )
            
            if event.type == pg.KEYUP and event.key == pg.K_SPACE and current_time <= 1 and self.shoots_counter < 2:
                self.shoot()
                self.shoots_counter += 1

    def set_direction(self, key):
        control = s.controls[key]
        self.image = st.rotate_sprite(self.aux_image, control['image_rotate'])
        self.shoot_direction = control['shoot_direction']
        self.shoot_speed = control['shoot_speed']

    def shoot(self):
        self.shoots.add(
            SpaceshipShoot(
                self.rect.center, 
                self.shoot_direction, 
                self.shoot_speed
            )
        )
    
    def update(self, free):
        current_timer = time.time()
        current_time = round(
            current_timer - self.inicial_shoot_timer, 
            1
        )
        if current_time > 1:
            self.inicial_shoot_timer = time.time()
            self.shoots_counter = 0

        self.actions(free)

class SpaceshipShoot(Sprite):
    def __init__(self, position, direction, shoot_speed):
        super().__init__()

        self.speed_x, self.speed_y = shoot_speed
        self.image = st.get_sprite(
            'spaceship_shoot_sprite',
            (30, 15),
            direction
        )
        self.rect = st.rect_sprite(self.image, position)

    def update(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.y > s.SCREEN_HEIGHT or self.rect.x > s.SCREEN_WIDTH:
            self.kill()