from characters.asteroid import Asteroid
from pygame.sprite import Group, groupcollide
import settings as s
import time

class AsteroidsLevel():
    def __init__(self):
        super().__init__()
        
        self.running = True
        self.asteroids_counter = 40
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
                2
            )
            
            if current_time == 1.5:
                for i in range(0, 6):
                    self.asteroids_counter -= 1
                    asteroid = Asteroid()
                    self.asteroids.append(asteroid)
                    self.asteroids_group.add(asteroid)
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

        collide_asteroid_spaceship = groupcollide(
            self.asteroids_group, 
            spaceship_group, 
            True, False
        )
        if collide_asteroid_spaceship:
            for spaceship in collide_asteroid_spaceship.values():
                hearts[spaceship[0].lives - 1].damage()
                score += -200
                spaceship[0].damage()

            for asteroid in collide_asteroid_spaceship.keys():
                asteroid.destroy()
                self.asteroids_group.remove(asteroid)

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
        destroyed_count = 0
        for asteroid in self.asteroids:
            if asteroid.destroyed:
                destroyed_count += 1
                
        all_destroyed = destroyed_count == len(self.asteroids)
            
        if self.asteroids_counter <= 0 and all_destroyed:
            self.running = False
            self.victory = True

    def check_end_screen(self):
        return False