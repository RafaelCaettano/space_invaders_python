from characters.asteroid import Asteroid
from pygame.sprite import Group, groupcollide
import settings as s
import time

class AsteroidsLevel():
    def __init__(self):
        super().__init__()
        
        self.running = True
        self.asteroids_counter = 300
        self.asteroids = []
        self.reset_shield = False
        self.reset_hearts = True
        self.has_shields = False
        self.spaceship_free = True
        self.victory = False
        self.inicial_asteroid_timer = time.time()
        self.asteroids_group = Group()

    def set_asteroids(self):
        if self.asteroids_counter > 0:
            current_timer = time.time()
            current_time = round(
                current_timer - self.inicial_asteroid_timer, 
                1
            )
            if current_time == 1.5:
                asteroid = Asteroid()
                self.asteroids.append(asteroid)
                self.asteroids_group.add(asteroid)
                self.asteroids_counter -= 1
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

        collide_spaceship_shoot_asteroid = groupcollide(
            spaceship_shoot_group, 
            self.asteroids_group, 
            True, True
        )
        if collide_spaceship_shoot_asteroid:
            for asteroid in collide_spaceship_shoot_asteroid.values():
                asteroid[0].destroy()
                self.asteroids_group.remove(asteroid[0])
                score += 100

        return score

    def check_end_level(self):
        all_destroyed = False
        for asteroid in self.asteroids:
            all_destroyed = asteroid.destroyed

        if self.asteroids_counter == 0 and all_destroyed:
            self.running = False
            self.victory = True

    def check_end_screen(self):
        return False