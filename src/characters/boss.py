import pygame as pg
from pygame.sprite import Sprite
from random import randint
import time

class AlienBoss(Sprite):
    def __init__(self, shoots, x, y):
        super().__init__()

        self.image = pg.transform.scale(
            pg.image.load('assets/images/boss_sprite.png'),
            (200,257)
        )            
        self.rect = self.image.get_rect(
            center=(x,y)
        )
        self.shoots = shoots
        self.dead = False
        self.lives = 15
        self.first_move = True
        self.inicial_move_timer = time.time()
        self.inicial_shoot_timer = time.time()
        self.physics()

    def physics(self):
        self.speed = 10
    
    def is_dead(self):
        self.dead = True
    
    def damage(self):
        self.dead -= 1
    
    def move(self):
        if not(self.dead):
            current_timer = time.time()
            current_time = round(
                current_timer - self.inicial_move_timer, 
                1
            )

            if self.first_move and current_time > 1:
                self.inicial_move_timer = current_timer
                self.first_move = False

            current_time = round(
                current_timer - self.inicial_move_timer, 
                1
            )

            if current_time == 4 or current_time == 2:
                self.rect.y += self.speed / 5

            if current_time == 2 or current_time == 3 or current_time == 6 or current_time == 7:
                self.rect.x += self.speed
            elif current_time == 1 or current_time == 4 or current_time == 5 or current_time == 8:
                self.rect.x -= self.speed
            elif current_time > 8:
                self.inicial_move_timer = current_timer

    def shoot(self):
        current_timer = time.time()
        current_time = round(
            current_timer - self.inicial_shoot_timer, 
            1
        )

        if current_time == 1.5 and not(self.dead):
            self.shoots.add(
                AlienBossShoot(*self.rect.center)
            )
            self.shoots.add(
                AlienBossShoot(*self.rect.center)
            )
            self.shoots.add(
                AlienBossShoot(*self.rect.center)
            )
            self.inicial_shoot_timer = current_timer
        elif current_time > 2:
            self.inicial_shoot_timer = current_timer
    
    def update(self):
        self.shoot()
        self.move()

class AlienBossShoot(Sprite):
    def __init__(self, x, y):
        super().__init__()

        if randint(1, 2) == 1:
            x += randint(0, 100)
            self.x_rand = randint(0, 5)
        else:
            x -= randint(0, 100)
            self.x_rand = randint(0, 5) * -1

        self.image = pg.transform.scale(
            pg.image.load('assets/images/boss_shoot_sprite.png'),
            (70,50)
        ) 
        self.image = pg.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect(
            center=(x, y + 50)
        )

    def update(self):
        self.rect.y += 7
        self.rect.x += self.x_rand
        if self.rect.y < 0:
            self.kill()
