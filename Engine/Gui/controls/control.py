from Engine.Utilities.logger import *
import pygame as pg
from Engine.Utilities.loop import *
from Engine.Scripts.events import *
import Engine.Scripts.events as events
from typing_extensions import Unpack, TypedDict
class control_kwargs(TypedDict):
    children: list
    position: tuple[float, float]
    size: tuple[float, float]
    parent: object
    surface: pg.Surface
    stretch: bool
    color: pg.Color
    path: str
    visible: bool

class control:
    def __init__(self, **kwargs : Unpack[control_kwargs]):
        self.parent = []
        self.children = []
        self.position = (0, 0)
        self.size = (100, 100)
        self.surface = pg.Surface(self.size)
        self.stretch = False
        self.color = pg.Color(255,255,255,255)
        self.path = ""
        self.visible = True
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        self.set_color(self.color)
        self.set_size(self.size)
        self.set_parent(self.parent)

        sign_draw(self.draw)

    def unsign_all(self):
        for f in update_methods:
            try:
                if f.__self__ is self: unsign_update(f)
            except: continue
        for f in draw_methods:
            try: 
                if f.__self__ is self: unsign_draw(f)
            except: continue
        for f in logic_methods:
            try:
                if f.__self__ is self: unsign_logic(f)
            except: continue


    def destroy(self):
        self.unsign_all()
        self.set_parent([])
        for i in self.children:
            i.unsign_all()
            del i
        del self

    def __is_top(self) -> bool:
        rtrn = True
        p = self.get_final_parent()
        for control in p.parent[p.parent.index(p):]:
            if control is p: continue
            if control.get_rect().collidepoint(pg.mouse.get_pos()):
                rtrn = False
                break
        return rtrn

    def on_clicked(self) -> bool:
        for event in events.event_list:
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1 and self.get_rect().collidepoint(pg.mouse.get_pos()):
                    if not self.__is_top(): return False
                    return True
        return False
    
    def is_clicked(self) -> bool:
        if pg.mouse.get_pressed(3)[0]:
            if self.get_rect().collidepoint(pg.mouse.get_pos()):
                if not self.__is_top(): return False
                return True
        return False
    
    def is_hovered(self) -> bool:
        if self.get_rect().collidepoint(pg.mouse.get_pos()):
            if not self.__is_top(): return False
            return True
        return False
    
    def draw(self):
        if self.parent == None:
             unsign_draw(self.draw)
             return
        self.set_size(self.size)
    
    def get_final_parent(self, ctrl = None):
        if ctrl == None: ctrl = self
        if isinstance(ctrl.parent, control):
            return self.get_final_parent(ctrl.parent)
        else:
            return ctrl

    
    def set_size(self, size : tuple[float, float]):
        screen_size = self.get_screen_size()
        if self.stretch:
            if self.surface.get_rect().size == screen_size: return
        else:
            if self.surface.get_rect().size == size: return
        self.size = size
        if self.stretch:
            self.surface = pg.transform.scale(self.surface, screen_size)
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
        if isinstance(self.parent, control):
            calculated_position = (
                self.parent.position[0] + self.position[0] * (self.parent.size[0]),
                self.parent.position[1] + self.position[1] * (self.parent.size[1]),
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
        if isinstance(self.parent, control):
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
        if isinstance(child, control):
            child.set_parent(self)
        else:
            fatal(f"{child} is not a control")

    def set_parent(self, parent):
        if isinstance(self.parent, list):
            if self.parent.__contains__(self):
                self.parent.remove(self)
        elif isinstance(self.parent, control):
            if self.parent.children.__contains__(self):
                self.parent.children.remove(self)
        self.parent = parent

        if isinstance(parent, list):
            parent.append(self)
        elif isinstance(parent, control):
            parent.children.append(self)
        else:
            fatal(f"{parent} - {type(parent).__name__} is not a list or control")
