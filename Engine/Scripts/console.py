import Engine.Scripts.events as events
from Engine.Scripts.commands import *
from Engine.Utilities.logger import *
import pygame as pg
from Engine.Utilities.loop import *

class Console:
    def __init__(self, screen : pg.Surface):
        sign_draw(self.draw)
        sign_update(self.update)
        self.text = ""
        self.screen = screen
        self.enabled = False
        self.text_color = (255,255,255)
        pg.font.init()
        self.font = pg.font.SysFont("Arial", 15)
        self.commands = Commands()
        self.shift = False
        self.last_command = ""

    def draw(self):
        if self.enabled:
            self.surface = pg.surface.Surface((self.screen.get_width(), 25)).convert_alpha()
            self.surface.fill((0, 0, 0, 128))
            size = pg.display.get_window_size()
            self.screen.blit(self.surface, (0, 0))
            self.text_surface = self.font.render(f'> {self.text}', True, self.text_color)
            self.screen.blit(self.text_surface, (0, 25/5))

    def update(self):
        for (event, key) in events.keyboard_list:
            if key == pg.K_BACKQUOTE or key == 1105 : #1105 = ё
                self.enabled = not self.enabled
                self.text = ""
                self.text_color = (255, 255, 255)
                return
            if self.enabled:
                if key == pg.K_UP:
                    if type(self.last_command) is str:
                        self.text = self.last_command
                elif key == pg.K_RETURN:
                    self.last_command = self.text
                    self.text = self.commands.process_command(self.text)
                    self.text_color = (128,128,128)
                    if self.text == None or self.text == 0:
                        self.enabled = False
                        self.text_color = (255, 255, 255)
                elif key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if type(self.text) is str:
                        self.text_color = (255, 255, 255)
                        self.text += event.unicode
                    else:
                        self.text_color = (255, 255, 255)
                        self.text = events.keyboard_event.unicode
                events.keyboard_list = []