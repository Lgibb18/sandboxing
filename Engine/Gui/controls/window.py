from Engine.Gui.controls.control import control
import pygame as pg
from Engine.Utilities.loop import *
from Engine.Utilities.utils import *
from Engine.Utilities.logger import *
from Engine.Utilities.gui_tools import *
import random

class window(control):
    __is_dragging : bool = False
    __drag_offset : tuple[float, float] = (0, 0)
    def __init__(self,
            position : tuple[float, float] = (0, 0),
            size : tuple[float, float] = (50, 50),
            stretch : bool = False, 
            color : pg.Color = pg.Color(255,255,255,255),
            path : str = "",
            parent = None):
        super().__init__(position, size, stretch, color, path, parent)
        sign_update(self.update)

    def is_dragging(self): return self.__is_dragging
    
    def update(self):
        if not pg.mouse.get_pressed(3)[0]:
            self.__is_dragging = False
        if type(self.parent) is not list: return
        if self.is_clicked() and not self.__is_dragging:
                rtrn = False
                for control in self.parent[self.parent.index(self):]:
                     if control is self: continue
                     if type(control) is window: 
                          if control.is_dragging() or control.get_rect().collidepoint(pg.mouse.get_pos()):
                               rtrn = True
                               break
                if rtrn: return   
                          
                          
                pos = gui_tools.screen_to_ui(pg.mouse.get_pos())
                self.__drag_offset = (
                    pos[0] - self.position[0],
                    pos[1] - self.position[1]
                    )
                self.__is_dragging = True
                if type(self.parent) is list:
                     self.parent.append(self.parent.pop(self.parent.index(self)))

        if self.__is_dragging: 
            pos = gui_tools.screen_to_ui(pg.mouse.get_pos())
            self.position = (
                pos[0] - self.__drag_offset[0],
                pos[1] - self.__drag_offset[1]
            )
