import Engine.Scripts.commands as commands
import Engine.Utilities.clock as clock
from Engine.Utilities.logger import *
from Engine.Utilities.loop import *
from pygame_gui.elements import *
import pygame as pg
class TestUICommand:
    def __init__(self, name):
        commands.all_commands[name] = self

    def process(self, args : list):
        ws = pg.display.get_window_size()
        rect = pg.Rect(0, 0,500,300)
        rect.center = (ws[0] / 2,ws[1] / 2)
        UIWindow(rect=rect, resizable=True, window_display_title="Shimmy shimmy yay, shimmy yay, shimmy ya")



Command = TestUICommand("test")