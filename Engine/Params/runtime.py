from Engine.Params.loop import *
import Engine.Scripts.events as events
import pygame as pg
from Engine.Utilities.logger import *
class Runtime:
    """Every runtime vars"""
    def __init__(self):
        sign_update(self.update)
        self.grid_placing : bool = False

    def update(self):
        for (_, key) in events.keyboard_list:
            if key == pg.K_g:
                self.grid_placing = not runtime.grid_placing

runtime = Runtime()