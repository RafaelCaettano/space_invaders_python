import pygame as pg
import settings as s
from characters.shield import Shield
from characters.spaceship import Spaceship
from characters.alien import AlienHorde
from characters.heart import Heart
from characters.button import Button
from characters.boss import AlienBoss
from pygame.sprite import Group, groupcollide
from pygame.locals import QUIT

class Control():
    def __init__(self):
        super().__init__()
        self.new()
        
    def new(self):
        self.score = 0
        self.lives = 3
        self.shields_count = 4
        self.level = 1
        self.running = True
        self.boss = False
        self.first_time_boss = True 
        self.all_sprites = []

        self.set_display()
        self.set_shields()
        self.set_aliens()
        self.set_spaceship()
        self.set_hearts()

    def set_display(self):
        self.display = pg.display.set_mode(s.SCREEN_SIZE, pg.RESIZABLE)
        self.background = pg.transform.scale(
            pg.image.load('assets/images/background.jpg'),
            s.SCREEN_SIZE
        )   
    
    def blit_display(self):
        self.display.blit(
            self.background, 
            (0, 0)
        )  

    def blit_text(self):
        font = pg.font.Font(s.FONT, 18)
        text = font.render('SCORE ' + str(self.score), True, s.WHITE)
        text_rect = text.get_rect()
        text_rect.center = (60, 30)

        self.display.blit(
            text, 
            text_rect
        )

    def set_shields(self):
        self.shields = []
        self.shield_group = Group()

        last_shield_x = 133.32
        for i in range(self.shields_count):
            shield = Shield(last_shield_x, 400)
            self.shield_group.add(shield)
            self.shields.append(shield)
            self.all_sprites.append(shield)
            last_shield_x += 177.76

    def set_spaceship(self):
        self.spaceship_shoot_group = Group()
        self.spaceship = Spaceship(self.spaceship_shoot_group)
        self.spaceship_group = Group(self.spaceship)
        self.all_sprites.append(self.spaceship)

    def set_alien_boss(self):
        self.alien_boss_shoot_group = Group()
        self.alien_boss = AlienBoss(self.alien_boss_shoot_group, 400, 0)
        self.alien_boss_group = Group(self.alien_boss)
        self.all_sprites.append(self.alien_boss)

    def set_aliens(self):
        self.alien_horde = AlienHorde()
        self.enemies_group = Group()
        self.enemies_shoot_group = Group()
        alien_horde = self.alien_horde.alien_group(self.enemies_shoot_group, 3)
        self.enemies_group.add(alien_horde)
        for alien_row in alien_horde:
            for alien in alien_row:
                self.all_sprites.append(alien)

    def set_fps(self):
        clock = pg.time.Clock()
        clock.tick(s.FPS)
    
    def draw(self):
        self.enemies_group.draw(self.display)
        self.shield_group.draw(self.display)
        self.spaceship_group.draw(self.display)
        self.enemies_shoot_group.draw(self.display)
        self.spaceship_shoot_group.draw(self.display)
        self.hearts_group.draw(self.display)
    
    def update(self):
        self.enemies_group.update()
        self.alien_horde.update()
        self.shield_group.update()
        self.spaceship_group.update()
        self.enemies_shoot_group.update()
        self.spaceship_shoot_group.update()
        self.hearts_group.update()

    def tela_inicial(self):
        pg.init()
        font = pg.font.Font(s.FONT, 40)
        title_text = font.render('SPACE INVADERS', True, s.WHITE)
        title_text_rect = title_text.get_rect()
        title_text_rect.center = (s.SCREEN_WIDTH/2, s.SCREEN_HEIGHT/2 - 150)

        play_button = Button(
            'JOGAR', 
            (325, 250), 
            (150, 50),
            20, 
            s.WHITE,
            s.BLACK
        )

        self.running = True
        while self.running:
            self.set_fps()
            self.blit_display()
            self.display.blit(
                title_text, 
                title_text_rect
            )

            self.display.blit(
                play_button.surface, 
                play_button.rect
            )

            mouse_pos = pg.mouse.get_pos()
            mouse_pressed = pg.mouse.get_pressed()

            if play_button.click(mouse_pos, mouse_pressed):
                self.main()

            for event in pg.event.get():  
                if event.type == QUIT:
                    self.running = False

            pg.display.update() 

    def game_over(self):
        font = pg.font.Font('assets/fonts/ChakraPetchBold.ttf', 40)
        game_over_text = font.render('GAME OVER', True, s.WHITE)
        game_over_text_rect = game_over_text.get_rect()
        game_over_text_rect.center = (s.SCREEN_WIDTH/2, s.SCREEN_HEIGHT/2 - 150)

        for sprite in self.all_sprites:
            sprite.kill()

        restart_button = Button(
            'RESTART', 
            (325, 250), 
            (150, 50),
            20, 
            s.WHITE,
            s.BLACK
        )

        exit_button = Button(
            'SAIR', 
            (325, 325), 
            (150, 50),
            20, 
            s.WHITE,
            s.BLACK
        )

        self.running = True
        while self.running:
            self.set_fps()
            self.blit_display()
            self.display.blit(
                game_over_text, 
                game_over_text_rect
            )

            self.display.blit(
                restart_button.surface, 
                restart_button.rect
            )

            self.display.blit(
                exit_button.surface, 
                exit_button.rect
            )

            mouse_pos = pg.mouse.get_pos()
            mouse_pressed = pg.mouse.get_pressed()

            if restart_button.click(mouse_pos, mouse_pressed):
                self.new()
                self.main()

            if exit_button.click(mouse_pos, mouse_pressed):
                self.running = False

            for event in pg.event.get():  
                if event.type == QUIT:
                    self.running = False

            pg.display.update() 

    def collide(self):
        groupcollide(
            self.spaceship_shoot_group, 
            self.shield_group, 
            True, False
        )

        groupcollide(
            self.enemies_shoot_group, 
            self.spaceship_shoot_group, 
            True, True
        )

        collide_enemy_shoot_spaceship = groupcollide(
            self.enemies_shoot_group, 
            self.spaceship_group, 
            True, False
        )
        if collide_enemy_shoot_spaceship:
            for spaceship in collide_enemy_shoot_spaceship.values():
                self.score -= 200
                self.hearts[self.lives - 1].damage()
                spaceship[0].lives -= 1
                self.lives -= 1

                if self.lives <= 0:
                    self.running = False
                    self.game_over()

        collide_shoot_enemy = groupcollide(
            self.spaceship_shoot_group, 
            self.enemies_group, 
            True, True
        )
        if collide_shoot_enemy:
            for alien in collide_shoot_enemy.values():
                self.score += 100
                self.alien_horde.aliens.remove(alien[0])
                self.alien_horde.sort_aliens()
                self.enemies_group.remove(alien[0])
                alien[0].is_dead()

        collide_enemy_shield = groupcollide(
            self.enemies_group, 
            self.shield_group, 
            True, False
        )
        if collide_enemy_shield:
            for shield in collide_enemy_shield.values():
                shield[0].damage()

        collide_enemy_shoot_shield = groupcollide(
            self.enemies_shoot_group, 
            self.shield_group, 
            True, False
        )
        if collide_enemy_shoot_shield:
            for shield in collide_enemy_shoot_shield.values():
                shield[0].damage()

        if self.boss:

            collide_boss_shoot_shield = groupcollide(
                self.alien_boss_shoot_group, 
                self.shield_group, 
                True, False
            )
            if collide_boss_shoot_shield:
                for shield in collide_boss_shoot_shield.values():
                    shield[0].damage()
                    print(shield[0].lives)

            collide_boss_shield = groupcollide(
                self.alien_boss_group, 
                self.shield_group, 
                True, False
            )
            if collide_boss_shield:
                for shield in collide_boss_shield.values():
                    shield[0].damage()

            collide_shoot_boss = groupcollide(
                self.spaceship_shoot_group, 
                self.alien_boss_group, 
                True, False
            )
            if collide_shoot_boss:
                for alien in collide_shoot_boss.values():
                    self.score += 100
                    self.alien_boss.damage()

            collide_boss_shoot_spaceship = groupcollide(
                self.alien_boss_shoot_group, 
                self.spaceship_group, 
                True, False
            )
            if collide_boss_shoot_spaceship:
                for spaceship in collide_boss_shoot_spaceship.values():
                    self.score -= 200
                    self.hearts[self.lives - 1].damage()
                    spaceship[0].lives -= 1
                    self.lives -= 1

                    if self.lives <= 0:
                        self.running = False
                        self.game_over()

    def set_hearts(self):
        self.hearts = []
        self.hearts_group = Group()

        for i in range(self.lives):
            heart = Heart((i + 1) * 35, 570)
            self.hearts.append(heart)
            self.hearts_group.add(heart)
            self.all_sprites.append(heart)

    def teste(self):
        for alien in self.alien_horde.aliens:
            self.enemies_group.remove(alien)

        for shield in self.shield_group:
            shield.kill()

        self.alien_horde.aliens.clear()

    def verify_number_aliens(self):
        if len(self.alien_horde.aliens) == 0:
            self.alien_boss_group.draw(self.display)
            self.alien_boss_shoot_group.draw(self.display)
            self.alien_boss.update()
            self.alien_boss_shoot_group.update()
            self.boss = True
        
        if self.first_time_boss:
            self.set_alien_boss()
            self.set_hearts()
            self.set_shields()
            self.first_time_boss = False

    def main(self):
        pg.init()
        #self.teste()
        while self.running:
            self.set_fps()
            self.blit_display()
            self.blit_text()
            self.draw()
            self.update()
            self.collide()
            self.verify_number_aliens()

            for event in pg.event.get():  
                if event.type == QUIT:
                    self.running = False
                    pg.quit()
            
            pg.display.update() 
