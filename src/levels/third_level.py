from characters.asteroid import Asteroid
from pygame.sprite import Group, groupcollide
import settings as s
import time

class ThirdLevel():
    def __init__(self):
        super().__init__()
        
        self.running = True
        self.asteroids_counter = 0
        self.inicial_asteroid_timer = time.time()
        self.asteroids_group = Group()

    def set_asteroids(self):
        current_timer = time.time()
        current_time = round(
            current_timer - self.inicial_asteroid_timer, 
            1
        )
        
        if current_time == 1.5:
            asteroid = Asteroid()
            self.asteroids_group.add(asteroid)
            self.asteroids_counter += 1
        elif current_time > 1.5:
            self.inicial_asteroid_timer = current_timer

    def clear(self):
        self.asteroids_group.empty()
    
    def update(self):
        self.asteroids_group.update()
        self.check_end_level()
        self.set_asteroids()
    
    def draw(self, display):
        self.asteroids_group.draw(display)

    def collide(self, spaceship_group, spaceship_shoot_group, shield_group, hearts):
        score = 0
        return score

    def check_end_level(self):
        if self.asteroids_counter == 30:
            self.running = False

    def check_end_screen(self):
        return False