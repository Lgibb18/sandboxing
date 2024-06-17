import pygame as pg
import Scripts.Engine.events as events
from Scripts.Engine.entities import *
from Scripts.Engine.camera import *
import Scripts.Engine.sprites as sprites
from Scripts.Engine.sprites import *
from Scripts.Engine.utils import *
class Cell:
    pos : tuple[int, int] = (0,0)
    def __init__(self, entity, surface, number):
        self.entity = entity
        self.surface : pg.Surface = surface
        self.number = number


class Inventory:
    def __init__(self, screen):
        self.screen = screen
        self.active = True
        self.cells = []

        n = 0
        for i in list(all_entities.values()):
            self.cells.append(Cell(i, i.entity.icon, n))
            n += 1

    def draw(self):
        if self.active:
            resolution = pg.display.get_window_size()
            self.tabSize = (resolution[0] / 5, resolution[1])
            self.surface = pg.Surface(self.tabSize).convert_alpha()
            self.surface.fill((128, 128, 128, 128))
            #self.screen.blit(self.surface, (0, 0))
            sprites.blit_layer(self.surface, (0,0), LAYER_7_UI)
            for cell in self.cells:
                b : pg.Surface = cell.surface
                b = pg.transform.scale(b, (self.tabSize[0] / 4, self.tabSize[0] / 4))
                column = cell.number - (int(cell.number / 3) * 3)
                line = (int(cell.number / 3))
                cell.pos = (
                    column * (self.tabSize[0] / 4) + ((self.tabSize[0] / 16) * (column + 1)),
                    line * (self.tabSize[0] / 4) + ((self.tabSize[0] / 16) * (line + 1))
                )
                sprites.blit_layer(b, cell.pos, LAYER_7_UI)



    def update(self):
        for cell in self.cells:
            rect = cell.surface.get_rect()
            if collision_check_topleft(pg.mouse.get_pos(), cell.pos, (self.tabSize[0] / 4, self.tabSize[0] / 4)):
                temp = pg.image.load("Sprites/white.png")
                temp =pg.transform.scale(temp, (self.tabSize[0] / 4, self.tabSize[0] / 4)).convert_alpha()
                temp.fill((0,255,0, 128))
                sprites.blit_layer(temp, cell.pos, LAYER_7_UI)
                print(cell.entity.entity.name)
        for key in events.keyboard_list:
            if key == pg.K_TAB:
                self.active = not self.active
            if key == pg.K_e:
                Instantiate("planks", Transform(camera.mouse_pos()))
