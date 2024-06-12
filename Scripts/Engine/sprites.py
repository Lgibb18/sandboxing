import random
import Scripts
import pygame as pg
import Scripts.Engine.camera as camera
from Scripts.Engine.utils import *
LAYER_0_UNDER_GROUND = 0
LAYER_1_GROUND = 1
LAYER_2_OVER_GROUND = 2
LAYER_3_UNDER_OBJECTS = 3
LAYER_4_OBJECTS = 4
LAYER_5_OVER_OBJECTS = 5
LAYER_6_UNDER_UI = 6
LAYER_7_UI = 7
LAYER_8_OVER_UI = 8

class Sprites:
    def __init__(self, screen):
        self.all_sprites = [pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group()]
        self.screen = screen

    def run_logic(self):
        for i in self.all_sprites:
            i.update()



    def draw(self):


        for i in self.all_sprites:
            for sprite in i.sprites():
                sprite.rect.x += camera.main.pos[0]
                sprite.rect.y += camera.main.pos[1]
            i.draw(self.screen)  # Draw the images of all sprites.


every_sprites = None


def mouse_pos():
    m = pg.mouse.get_pos()
    return (m[0] - camera.main.pos[0], m[1] - camera.main.pos[1])