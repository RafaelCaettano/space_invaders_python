from pygame.sprite import Group, groupcollide
from characters.boss import AlienBoss

class SecondLevel():
    def __init__(self):
        super().__init__()
        
        self.running = True
        self.set_alien_boss()
    
    def set_alien_boss(self):
        self.alien_boss_shoot_group = Group()
        self.alien_boss = AlienBoss(self.alien_boss_shoot_group, 400, 0)
        self.alien_boss_group = Group(self.alien_boss)

    def clear(self):
        self.alien_boss_shoot_group.empty()
        self.alien_boss_group.empty()
        self.alien_boss = AlienBoss(self.alien_boss_shoot_group, 400, 0)
    
    def update(self):
        self.alien_boss_group.update()
        self.alien_boss_shoot_group.update()
        self.check_end_level()
    
    def draw(self, display):
        self.alien_boss_group.draw(display)
        self.alien_boss_shoot_group.draw(display)
    
    def collide(self, spaceship_group, spaceship_shoot_group, shield_group, hearts):
        score = 0

        collide_boss_shoot_shield = groupcollide(
            self.alien_boss_shoot_group, 
            shield_group, 
            True, False
        )
        if collide_boss_shoot_shield:
            for shield in collide_boss_shoot_shield.values():
                shield[0].damage()

        collide_boss_shield = groupcollide(
            self.alien_boss_group, 
            shield_group, 
            False, False
        )
        if collide_boss_shield:
            for shield in collide_boss_shield.values():
                shield[0].damage()
                self.alien_boss.damage()

        collide_shoot_boss = groupcollide(
            spaceship_shoot_group, 
            self.alien_boss_group, 
            True, False
        )
        if collide_shoot_boss:
            score += 100
            self.alien_boss.damage()

        collide_boss_shoot_spaceship = groupcollide(
            self.alien_boss_shoot_group, 
            spaceship_group, 
            True, False
        )
        if collide_boss_shoot_spaceship:
            for spaceship in collide_boss_shoot_spaceship.values():
                score -= 200
                hearts[spaceship[0].lives - 1].damage()
                spaceship[0].lives -= 1

        return score

    def check_end_level(self):
        if self.alien_boss.lives == 0:
            self.running = False
