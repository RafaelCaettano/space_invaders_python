import pygame as pg
from pygame.sprite import Sprite
from pygame.locals import QUIT
import time

class Spaceship(Sprite):
    def __init__(self, shoots):
        super().__init__()

        self.image = pg.transform.scale(
            pg.image.load('assets/images/spaceship_sprite.png'),
            (55,70)
        )            
        self.rect = self.image.get_rect(
            center=(400,520)
        )
        self.shoots = shoots
        self.shoots_counter = 0
        self.inicial_shoot_timer = time.time()
        self.counters()
        self.physics()
    
    def counters(self):
        self.lives = 3
        self.shoots_number = 0

    def physics(self):
        self.speed = 3
    
    def actions(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.x < 745:
            self.rect.x += self.speed
            
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

    def shoot(self):
        self.shoots.add(
            SpaceshipShoot(*self.rect.center)
        )
    
    def update(self):
        current_timer = time.time()
        current_time = round(
            current_timer - self.inicial_shoot_timer, 
            1
        )
        if current_time > 1:
            self.inicial_shoot_timer = time.time()
            self.shoots_counter = 0

        self.actions()

class SpaceshipShoot(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pg.transform.scale(
            pg.image.load('assets/images/spaceship_shoot_sprite.png'),
            (30,15)
        ) 
        self.image = pg.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect(
            center=(x, y)
        )

    def update(self):
        self.rect.y -= 7
        if self.rect.y > 600:
            self.kill()