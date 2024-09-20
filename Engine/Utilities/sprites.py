import Engine.Scripts.camera as camera
import pygame as pg
import asyncio
import Engine
import Engine.Utilities
from Engine.Utilities.loop import *

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
        sign_logic(self.run_logic)
        sign_draw(self.draw)
        self.all_sprites = [pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group(),
                            pg.sprite.Group()]
        self.screen : pg.Surface = screen

    def run_logic(self):
        for i in self.all_sprites:
            i.update()



    def draw(self):
        asyncio.run(self.draw_async())

    async def draw_async(self):
        n = 0
        for i in self.all_sprites:
            if n not in disabled_layers:
                if(len(i.sprites()) > 0):
                    for sprite in i.sprites():
                        sprite.rect.x += camera.main.pos[0]
                        sprite.rect.y += camera.main.pos[1]
                    i.draw(self.screen)  # Draw the images of all sprites.
                if len(Engine.Utilities.sprites.to_blit) > 8:
                    for surf in Engine.Utilities.sprites.to_blit[n]:
                        self.screen.blit(surf[0], surf[1])
            n += 1
        Engine.Utilities.sprites.to_blit = [
            [], # 1
            [], # 2
            [], # 3
            [], # 4
            [], # 5
            [], # 6
            [], # 7
            [], # 8
            []  # 9
        ]

every_sprites : Sprites = None
disabled_layers = []
to_blit : list[list[tuple[pg.Surface, tuple[int, int]]]] = [
    [], # 1
    [], # 2
    [], # 3
    [], # 4
    [], # 5
    [], # 6
    [], # 7
    [], # 8
    []  # 0
]
def blit_layer(surface : pg.Surface, pos : tuple[int, int], layer : int):
    if layer not in disabled_layers:
        if layer in range(0,9):
            to_blit[layer].append((surface, pos))

def mouse_pos():
    m = pg.mouse.get_pos()
    return (m[0] - camera.main.pos[0], m[1] - camera.main.pos[1])