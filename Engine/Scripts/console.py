import Engine.Scripts.events as events
from Engine.Scripts.commands import *


class Console:
    def __init__(self, screen : pg.Surface):
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
        special_keys = [pg.K_BACKSPACE, pg.K_RETURN, pg.K_SPACE, pg.K_LSHIFT]
        for key in events.keyboard_list:
            if self.enabled:
                if self.text == "" or self.text == None:
                    self.text_color = (255, 255, 255)
                if key not in special_keys:
                    if self.shift:
                        self.text += pg.key.name(key).upper()
                    else:
                        #self.text += pg.key.name(key)
                        if type(self.text) is str:
                            self.text += events.keyboard_event.unicode
                        else:
                            self.text_color = (255, 255, 255)
                            self.text = events.keyboard_event.unicode
                if key == pg.K_BACKSPACE:
                    if type(self.text) is str:
                        self.text = self.text[:-1]
                    else:
                        self.text_color = (255, 255, 255)
                        self.text = ""
                if key == pg.K_RETURN:
                    if type(self.text) is str:
                        self.last_command = self.text
                        self.text = self.commands.process_command(self.text)
                        self.text_color = (128,128,128)
                        if self.text == None or self.text == 0:
                            self.enabled = False
                            self.text_color = (255, 255, 255)
                    else:
                        self.enabled = not self.enabled
                        self.text = ""
                        self.text_color = (255, 255, 255)
                if key == pg.K_SPACE:
                    if type(self.text) is str:
                        self.text += " "
                    else:
                        self.text_color = (255, 255, 255)
                        self.text = ""
                if key == pg.K_LSHIFT:
                    self.shift = True
                if key != pg.K_LSHIFT:
                    self.shift = False
                if key == pg.K_UP:
                    self.text = self.last_command
                    self.text_color = (255, 255, 255)
                events.keyboard_list = []
            if key == pg.K_BACKQUOTE or key == 1105 : #1105 = ё
                self.enabled = not self.enabled
                self.text = ""
                self.text_color = (255, 255, 255)