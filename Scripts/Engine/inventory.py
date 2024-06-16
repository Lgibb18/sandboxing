import pygame as pg
import Scripts.Engine.events as events

class Inventory:
    def __init__(self, screen):
        self.screen = screen
        self.active = True


    def draw(self):
        if self.active:
            resolution = pg.display.get_window_size()
            self.surface = pg.Surface((resolution[0] / 5, resolution[1])).convert_alpha()
            self.surface.fill((128, 128, 128, 128))
            self.screen.blit(self.surface, (0, 0))

    def update(self):
        for key in events.keyboard_list:
            if key == pg.K_TAB:
                self.active = not self.active
