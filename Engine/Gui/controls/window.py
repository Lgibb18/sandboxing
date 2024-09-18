from Engine.Gui.controls.control import *
from typing_extensions import Unpack

import pygame as pg
from Engine.Utilities.loop import *
from Engine.Utilities.utils import *
from Engine.Utilities.logger import *
from Engine.Utilities.gui_tools import *
import random

class window(control):
    __is_dragging : bool = False
    __is_clicking : bool = False
    __drag_offset : tuple[float, float] = (0, 0)
    def __init__(self, **kwargs: Unpack[control_kwargs]):
        super().__init__(kwargs)
        sign_update(self.update)

    def is_dragging(self): return self.__is_dragging
    
    def update(self):
        if not pg.mouse.get_pressed(3)[0]:
            self.__is_dragging = False
            self.__is_clicking = False
        if type(self.parent) is not list: return
        if self.is_clicked() and not self.__is_dragging and not self.__is_clicking:
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
        if pg.mouse.get_pressed(3)[0]: self.__is_clicking = True
        if self.__is_dragging: 
            pos = gui_tools.screen_to_ui(pg.mouse.get_pos())
            self.position = (
                pos[0] - self.__drag_offset[0],
                pos[1] - self.__drag_offset[1]
            )
