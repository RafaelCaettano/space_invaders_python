import pygame as pg
import settings as s
from components.button import Button
from pygame.locals import QUIT
from components.label import Label
from display import Display

class VictoryScreen():
    def __init__(self):
        self.display = Display()
        self.new()

    def new(self):
        self.display.set_display()

    def load(self, start):
        victory_label = Label(
            'VOCÊ GANHOU!',
            40,
            (s.SCREEN_WIDTH/2, s.SCREEN_HEIGHT/2 - 150),
            s.WHITE
        )

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
            self.display.set_fps()
            self.display.blit_display()
            self.display.blit_text(victory_label)
            self.display.blit_button(restart_button)
            self.display.blit_button(exit_button)

            mouse_pos = pg.mouse.get_pos()
            mouse_pressed = pg.mouse.get_pressed()

            if restart_button.click(mouse_pos, mouse_pressed):
                start()

            if exit_button.click(mouse_pos, mouse_pressed):
                self.running = False
                pg.quit()

            for event in pg.event.get():  
                if event.type == QUIT:
                    pg.quit()
                    self.running = False

            pg.display.update() 
