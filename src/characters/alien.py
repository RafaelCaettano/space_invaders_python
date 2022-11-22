import pygame as pg
from pygame.sprite import Sprite
from random import randint
import time
from tools import sprite_tools as st

class Alien(Sprite):
    def __init__(self, shoots, position):
        super().__init__()

        self.image = st.get_sprite(
            'alien_sprite',
            (22, 30)
        ) 
        self.rect = st.rect_sprite(self.image, position)

        self.shoots = shoots
        self.dead = False
        self.first_move = True
        self.inicial_move_timer = time.time()
        self.physics()

    def physics(self):
        self.speed = 2
    
    def is_dead(self):
        self.dead = True
        self.kill()
    
    def move(self):
        if not(self.dead):
            current_timer = time.time()
            current_time = round(
                current_timer - self.inicial_move_timer, 
                1
            )

            if current_time == 4 or current_time == 2:
                self.rect.y += self.speed / 2

            if current_time == 2 or current_time == 3 or current_time == 6 or current_time == 7:
                self.rect.x += self.speed * 2
            elif current_time == 1 or current_time == 4 or current_time == 5 or current_time == 8:
                self.rect.x -= self.speed * 2
            elif current_time > 8:
                self.inicial_move_timer = current_timer

    def shoot(self):
        if not(self.dead):
            self.shoots.add(
                AlienShoot(self.rect.center)
            )
    
    def update(self):
        self.move()

class AlienShoot(Sprite):
    def __init__(self, position):
        super().__init__()

        self.image = st.get_sprite(
            'alien_shoot_sprite',
            (30, 15),
            270
        ) 
        self.rect = st.rect_sprite(self.image, position)

    def update(self):
        self.rect.y += 7
        if self.rect.y < 0:
            self.kill()

class AlienHorde():
    def __init__(self):
        self.aliens = []
        self.inicial_shoot_timer = time.time()

    def shoot(self):
        current_timer = time.time()
        current_time = round(
            current_timer - self.inicial_shoot_timer, 
            1
        )
        
        if current_time == 1.5 and len(self.aliens) > 0:
            i = randint(0, len(self.aliens) - 1)
            self.aliens[i].shoot()
            self.inicial_shoot_timer = current_timer
        elif current_time > 1.5:
            self.inicial_shoot_timer = current_timer
        

    def sort_aliens(self):
        self.aliens.sort(key=resort) 

    def alien_group(self, group, lines):
        aliens_row = []
        alien_matrix = []
        
        for i in range(50, lines * 75, 75):
            for j in range(100, 700, 65):
                alien = Alien(group, (j, i))
                self.aliens.append(alien)
                aliens_row.append(
                    alien
                )
            alien_matrix.append(aliens_row)
        
        return alien_matrix

    def update(self):
        self.shoot()

def resort(e):
    return not(e.dead)