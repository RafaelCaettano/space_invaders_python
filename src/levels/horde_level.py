from characters.alien import AlienHorde
from pygame.sprite import Group, groupcollide
import settings as s

class HordeLevel():
    def __init__(self):
        super().__init__()
        
        self.running = True
        self.reset_shield = True
        self.reset_hearts = True
        self.has_shields = True
        self.spaceship_free = False
        self.victory = False
        self.set_aliens()

    def set_aliens(self):
        self.alien_horde = AlienHorde()
        self.aliens_group = Group()
        self.aliens_shoot_group = Group()
        alien_horde = self.alien_horde.alien_group(self.aliens_shoot_group, 3)
        self.aliens_group.add(alien_horde)

    def clear(self):
        self.aliens_shoot_group.empty()
        self.aliens_group.empty()
        self.alien_horde = AlienHorde()
    
    def update(self):
        self.aliens_group.update()
        self.aliens_shoot_group.update()
        self.alien_horde.update()
        self.check_end_level()
    
    def draw(self, display):
        self.aliens_group.draw(display)
        self.aliens_shoot_group.draw(display)

    def collide(self, spaceship_group, spaceship_shoot_group, shield_group, hearts):
        score = 0
        
        groupcollide(
            self.aliens_shoot_group, 
            spaceship_shoot_group, 
            True, True
        )

        collide_enemy_shoot_spaceship = groupcollide(
            self.aliens_shoot_group, 
            spaceship_group, 
            True, False
        )
        if collide_enemy_shoot_spaceship:
            for spaceship in collide_enemy_shoot_spaceship.values():
                hearts[spaceship[0].lives - 1].damage()
                spaceship[0].damage()
                score += -200

        collide_enemy_spaceship = groupcollide(
            self.aliens_group, 
            spaceship_group, 
            True, False
        )
        if collide_enemy_spaceship:
            for spaceship in collide_enemy_spaceship.values():
                hearts[spaceship[0].lives - 1].damage()
                spaceship[0].damage()
                score += -200

        collide_enemy_shield = groupcollide(
            self.aliens_group, 
            shield_group, 
            True, False
        )
        if collide_enemy_shield:
            for shield in collide_enemy_shield.values():
                shield[0].damage()

        collide_enemy_shoot_shield = groupcollide(
            self.aliens_shoot_group, 
            shield_group, 
            True, False
        )
        if collide_enemy_shoot_shield:
            for shield in collide_enemy_shoot_shield.values():
                shield[0].damage()

        collide_spaceship_shoot_enemy = groupcollide(
            spaceship_shoot_group, 
            self.aliens_group, 
            True, True
        )
        if collide_spaceship_shoot_enemy:
            for alien in collide_spaceship_shoot_enemy.values():
                alien[0].is_dead()
                self.alien_horde.aliens.remove(alien[0])
                self.alien_horde.sort_aliens()
                self.aliens_group.remove(alien[0])
                score += 100
        
        return score

    def check_end_level(self):
        if len(self.alien_horde.aliens) == 0:
            self.victory = True
            self.running = False

    def check_end_screen(self):
        end_screen = False

        for alien in self.alien_horde.aliens:
            if alien.rect.y > s.SCREEN_HEIGHT:
                end_screen = True
        
        return end_screen