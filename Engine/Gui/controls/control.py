from Engine.Utilities.logger import *
import pygame as pg
from Engine.Utilities.loop import *
from Engine.Scripts.events import *
import functools
from typing_extensions import Unpack, TypedDict

class control_kwargs(TypedDict):
    children : list
    position : tuple[float, float]
    size : tuple[float, float]
    parent : object
    surface : pg.Surface
    stretch : bool
    color : pg.Color
    path : str

class control:
    def __init__(self, **kwargs : Unpack[control_kwargs]):
        self.children : list
        self.position : tuple[float, float]
        self.size : tuple[float, float]
        self.parent : control | list
        self.surface : pg.Surface
        self.stretch : bool
        self.color : pg.Color
        self.path : str
        for key, value in kwargs:
            self.__setattr__(key, value)
        
        
        #self.position = position
        #self.size = size
        #self.stretch = stretch
        #self.path = path
        #self.children = []
        #self.surface = pg.Surface(size)
        #self.visible = visible

        self.set_size(self.size)
        self.set_parent(self.parent)
        self.set_color(self.color)

        sign_draw(self.draw)

    def on_clicked(self) -> bool:
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1 and self.get_rect().collidepoint(pg.mouse.get_pos()):
                    return True
        return False
    
    def is_clicked(self) -> bool:
        if pg.mouse.get_pressed(3)[0]:
            if self.get_rect().collidepoint(pg.mouse.get_pos()):
                return True
        return False
    
    def draw(self):
        self.set_size(self.size)
    
    def get_final_parent(self, control = None):
        if control == None: control = self
        if type(control.parent) is control:
            return self.get_final_parent(control.parent)
        else:
            return control

    
    def set_size(self, size : tuple[float, float]):
        if self.surface.get_rect().size == size: return
        self.size = size
        if self.stretch:
            self.surface = pg.transform.scale(self.surface, self.get_screen_size())
        else:
            self.surface = pg.transform.scale(self.surface, self.size)

    def set_color(self, color : pg.Color):
        self.color = color
        if self.path == "": self.surface.fill(self.color)
        else: 
            self.surface = pg.image.load(self.path)
            self.surface.fill(self.color, special_flags=pg.BLEND_RGB_MULT)
        self.surface.convert_alpha()
        
    
    def get_rect(self):
        screen_position = self.get_screen_pos()
        screen_size = self.get_screen_size()
        return pg.Rect(screen_position[0], screen_position[1], screen_size[0], screen_size[1])

    def get_screen_pos(self):
        position = self.position
        resolution = pg.display.get_window_size()
        screen_size = self.get_screen_size()
        if type(self.parent) is control:
            calculated_position = (
                self.parent.position[0] + self.position[0] * (self.parent.size[0] / resolution[0]),
                self.parent.position[1] + self.position[1] * (self.parent.size[1] / resolution[1]),
            )
            position = (
                resolution[0] / 2 + resolution[0] / 2 *  calculated_position[0] - screen_size[0] / 2,
                resolution[1] / 2 + resolution[1] / 2 * -calculated_position[1] - screen_size[1] / 2,
            )
        else:
            position = (
                resolution[0] / 2 + resolution[0] / 2 *  self.position[0] - screen_size[0] / 2,
                resolution[1] / 2 + resolution[1] / 2 * -self.position[1] - screen_size[1] / 2,
            )
        return position
    

    def get_screen_size(self):
        if not self.stretch: return self.size
        size = self.size
        resolution = pg.display.get_window_size()
        if type(self.parent) is control:
            size = (
                resolution[0] * self.size[0] * self.parent.size[0],
                resolution[1] * self.size[1] * self.parent.size[1]
            )
        else:
            size = (
                resolution[0] * self.size[0],
                resolution[1] * self.size[1],
            )
        return size

    
    def get_local_pos(self, position : tuple[int, int]):
        rect = self.get_rect()
        screen_size = self.get_screen_size()
        return (
             ((position[0] - rect.centerx) / (screen_size[0] / 2)),
            -((position[1] - rect.centery) / (screen_size[1] / 2)),
        )
    
    def add_child(self, child):
        if type(child) is control:
            child.set_parent(self)
        else:
            fatal(f"{child} is not a control")

    def set_parent(self, parent):
        self.parent = parent

        if type(parent) is list:
            parent.append(self)
        elif type(parent) is control:
            parent.children.append(self)
        else:
            fatal(f"{parent} - {type(parent).__name__} is not a list or control")
