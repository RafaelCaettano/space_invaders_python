import pygame as pg
import settings as s
from characters.shield import Shield
from characters.spaceship import Spaceship
from characters.heart import Heart
from pygame.sprite import Group, groupcollide
from pygame.locals import QUIT
from levels.horde_level import HordeLevel
from levels.alien_boss_level import AlienBossLevel
from levels.asteroids_level import AsteroidsLevel
from components.label import Label
from display import Display
from screens.initial_screen import InitialScreen
from screens.game_over_screen import GameOverScreen
from screens.victory_screen import VictoryScreen

class Control():
    def __init__(self):
        self.display = Display()
        self.screen = InitialScreen()
        
    def new(self):
        self.score = 0
        self.level_number = 0
        self.running = True
        self.all_sprites = []

        self.set_levels()
        self.display.set_display()
        self.set_spaceship()
        self.set_shields()
        self.set_hearts()

    def set_levels(self):
        first = HordeLevel()
        second = AsteroidsLevel()
        third = AlienBossLevel()
        self.levels = [
            second,
            first,
            third,
        ]

        self.level = self.levels[self.level_number]

    def set_shields(self):
        self.shields = []
        self.shield_group = Group()

        if self.level.has_shields:
            self.shields_count = 4
            last_shield_x = 133.32
            for i in range(self.shields_count):
                shield = Shield((last_shield_x, 400))
                self.shield_group.add(shield)
                self.shields.append(shield)
                self.all_sprites.append(shield)
                last_shield_x += 177.76
        else:
            self.shields_count = 0
            self.shields = []
            self.shield_group.empty()

    def set_spaceship(self):
        self.spaceship_shoot_group = Group()
        self.spaceship = Spaceship(self.spaceship_shoot_group)
        self.spaceship_group = Group(self.spaceship)
        self.all_sprites.append(self.spaceship)

    def set_hearts(self):
        if self.level.reset_hearts:
            self.hearts = []
            self.hearts_group = Group()
            self.spaceship.lives = 3
            for i in range(self.spaceship.lives):
                heart = Heart(((i + 1) * 35, 570))
                self.hearts.append(heart)
                self.hearts_group.add(heart)
                self.all_sprites.append(heart)
    
    def draw(self):
        self.shield_group.draw(self.display.screen)
        self.spaceship_group.draw(self.display.screen)
        self.spaceship_shoot_group.draw(self.display.screen)
        self.hearts_group.draw(self.display.screen)
        self.level.draw(self.display.screen)
    
    def update(self):
        self.shield_group.update()
        self.spaceship_group.update(self.level.spaceship_free)
        self.spaceship_shoot_group.update()
        self.hearts_group.update()
        self.level.update()

    def collide(self):
        self.score += self.level.collide(
            self.spaceship_group,
            self.spaceship_shoot_group,
            self.shield_group,
            self.hearts
        )

        self.shield_collide()

    def shield_collide(self):
        if self.level.has_shields:
            groupcollide(
                self.spaceship_shoot_group, 
                self.shield_group, 
                True, False
            )

    def show_score(self):
        score_label = Label(
            'SCORE ' + str(self.score),
            18,
            (60, 30),
            s.WHITE
        )
            
        self.display.blit_text(score_label)

    def main(self):
        self.screen.load(self.start)

    def start(self):
        self.new()
        while self.running:
            self.display.set_fps()
            self.display.blit_display()
            self.show_score()
            self.draw()
            self.update()
            self.collide()
            self.check_end_level()
            self.check_game_over()

            for event in pg.event.get():  
                if event.type == QUIT:
                    self.running = False
                    pg.quit()
            
            pg.display.update() 

    def check_end_level(self):
        if not(self.level.running) and self.level.victory:
            if len(self.levels) > self.level_number + 1:
                self.next_level()
            else:
                self.victory()

    def check_game_over(self):
        if self.level.check_end_screen():
            self.game_over()

        if self.spaceship.lives == 0:
            self.game_over()

    def next_level(self):
        self.level.clear()
        self.level_number += 1
        self.level = self.levels[self.level_number]
        self.set_spaceship()
        self.set_shields()
        self.set_hearts()

    def game_over(self):
        self.screen = GameOverScreen()
        self.main()

    def victory(self):
        self.screen = VictoryScreen()
        self.main()

    
