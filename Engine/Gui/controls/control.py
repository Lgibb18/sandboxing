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
    stretchX: bool
    stretchY: bool
    color: pg.Color
    path: str
    visible: bool
    strictSize: bool
    name: str

class control:
    def __init__(self, **kwargs : Unpack[control_kwargs]):
        self.name = __name__
        self.parent = []
        self.children = []
        self.position = (0, 0)
        self.size = (100, 100)
        self.surface = pg.Surface(self.size)
        self.surface = self.surface.convert_alpha()
        self.stretchX = False
        self.stretchY = False
        self.color = pg.Color(255,255,255,255)
        self.path = ""
        self.visible = True
        self.strictSize = False
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
        p = self.get_absolute_parent()
        for control in p.parent[p.parent.index(p):]:
            if control is p: continue
            if control.get_rect().collidepoint(pg.mouse.get_pos()):
                rtrn = False
                break
        return rtrn

    def on_clicked(self, on_surface : bool = False) -> bool:
        for event in events.event_list:
            if event.type == pg.MOUSEBUTTONUP:
                rect = self.get_rect()
                if on_surface:
                    screen_pos = self.get_screen_pos()
                    rect = self.get_rect(screen_pos, self.surface.get_rect().size)
                if event.button == 1 and rect.collidepoint(pg.mouse.get_pos()):
                    if not self.__is_top(): return False
                    return True
        return False
    
    def is_clicked(self, on_surface : bool = False) -> bool:
        rect = self.get_rect()
        if on_surface:
            screen_pos = self.get_screen_pos()
            rect = self.get_rect(screen_pos, self.surface.get_rect().size)
        if pg.mouse.get_pressed(3)[0]:
            if rect.collidepoint(pg.mouse.get_pos()):
                if not self.__is_top(): return False
                return True
        return False
    
    def is_hovered(self, on_surface : bool = False) -> bool:
        rect = self.get_rect()
        if on_surface:
            screen_pos = self.get_screen_pos()
            rect = self.get_rect(screen_pos, self.surface.get_rect().size)
        if rect.collidepoint(pg.mouse.get_pos()):
            if not self.__is_top(): return False
            return True
        return False
    
    def draw(self):
        if self.parent == None:
             unsign_draw(self.draw)
             return
        self.set_size(self.size)
    
    def get_absolute_parent(self, ctrl = None):
        if ctrl == None: ctrl = self
        if isinstance(ctrl.parent, control):
            return self.get_absolute_parent(ctrl.parent)
        else:
            return ctrl

    def get_all_parents(self, ctrl = None, parents : list = []):
        if ctrl == None: ctrl = self
        if isinstance(ctrl.parent, control):
            return self.get_all_parents(ctrl.parent, parents + [ctrl.parent])
        else:
            return parents

    
    def set_size(self, size : tuple[float, float]):
        screen_size = self.get_screen_size()
        if self.stretchX or self.stretchY:
            if self.surface.get_rect().size == screen_size: return
        else:
            if self.surface.get_rect().size == size: return
        self.size = size
        if self.stretchX or self.stretchY:
            self.surface = pg.transform.scale(self.surface, screen_size)
        else:
            self.surface = pg.transform.scale(self.surface, self.size)

    def set_size_dont_update(self, size : tuple[float, float]):
        screen_size = self.get_screen_size(size)
        if self.stretchX or self.stretchY:
            if self.surface.get_rect().size == screen_size: return
        else:
            if self.surface.get_rect().size == size: return
        if self.stretchX or self.stretchY:
            self.surface = pg.transform.scale(self.surface, screen_size)
        else:
            self.surface = pg.transform.scale(self.surface, size)

    def set_size_dont_update_resolution(self, size : tuple[float, float], resolution : float):
        screen_size = self.get_screen_size_resolution(size, resolution)
        if self.stretchX or self.stretchY:
            if self.surface.get_rect().size == screen_size: return
        else:
            if self.surface.get_rect().size == size: return
        if self.stretchX or self.stretchY:
            self.surface = pg.transform.scale(self.surface, screen_size)
        else:
            self.surface = pg.transform.scale(self.surface, size)

    def set_color(self, color : pg.Color):
        self.color = color
        if self.path == "": self.surface.fill(self.color)
        else: 
            self.surface = pg.image.load(self.path)
            self.surface.fill(self.color, special_flags=pg.BLEND_RGB_MULT)
        self.surface = self.surface.convert_alpha()
        
    
    def get_rect(self, screen_position = None, screen_size = None):
        if screen_position == None: screen_position = self.get_screen_pos()
        if screen_size == None: screen_size = self.get_screen_size()
        return pg.Rect(screen_position[0], screen_position[1], screen_size[0], screen_size[1])
    
    def calculate_parent_pos(self, cntrl = None, position = None, i = 0):
        if cntrl == None: cntrl = self
        if position == None: position = cntrl.position
        if isinstance(cntrl.parent, list):
            return position
        parent_size = self.parent.convert_size_to_stretch()
        calculated_pos = (
                cntrl.parent.position[0] + position[0] * (parent_size[0]),
                cntrl.parent.position[1] + position[1] * (parent_size[1]),
            )
        if isinstance(cntrl.parent, control):
            pos = self.calculate_parent_pos(cntrl.parent, calculated_pos, i+1)
            return pos
        return calculated_pos
    

    def calculate_position(self, cntrl = None, position = None, cur_parent = None):
        all_parents = self.get_all_parents()
        all_parents.reverse()
        i = -1
        cur_pos = self.position
        for parent in all_parents:
            i += 1
            if isinstance(parent, list):
                break
            elif not isinstance(parent, control): break
            cur_pos = (
                (parent.convert_size_to_stretch()[0] * cur_pos[0]) * parent.position[0] + (cur_pos[0] * parent.convert_size_to_stretch()[0]),
                (parent.convert_size_to_stretch()[1] * cur_pos[1]) * parent.position[1] + (cur_pos[1] * parent.convert_size_to_stretch()[1]),
            )
        return cur_pos



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
    
    def screen_diff(self):
        window_size = pg.display.get_window_size()
        if self.strictSize: return (1, 1)
        return (
            window_size[0] / 1280,
            window_size[1] / 720
        )

    def multiply_every_parent_size(self, cntrl = None, size = None):
        if cntrl == None: cntrl = self
        if size == None: size = cntrl.size

        if isinstance(cntrl.parent, control):
            return self.multiply_every_parent_size(cntrl.parent, (cntrl.parent.size[0] * size[0], cntrl.parent.size[1] * size[1]))
        return size
    

    def convert_size_to_stretch(self, size = None):
        if size == None: size = self.size
        _size = self.size
        _parent_size = pg.display.get_window_size()
        if isinstance(self.parent, control):
            _parent_size = self.parent.get_screen_size()
        if not self.stretchX:
            _size = (
                self.size[0] / _parent_size[0],
                _size[1]
            )
        if not self.stretchY:
            _size = (
                _size[0],
                self.size[1] / _parent_size[1],
            )
        return _size


    def get_screen_size(self, size = None):
        if size == None: size = self.size
        if (not self.stretchX) and (not self.stretchY): return (
            size[0] * self.screen_diff()[0],
            size[1] * self.screen_diff()[1]
        )
    
        _size = self.size
        resolution = pg.display.get_window_size()
        absolute_parent = self.get_absolute_parent()
        if isinstance(self.parent, control):
            _size = (
                resolution[0] * size[0] * self.multiply_every_parent_size()[0],
                resolution[1] * size[1] * self.multiply_every_parent_size()[1]
            )
        else:
            _size = (
                resolution[0] * self.size[0],
                resolution[1] * self.size[1],
            )
        if not self.stretchX: 
            _size = (self.size[0] * self.screen_diff()[0], _size[1])
        if not self.stretchY: 
            _size = (_size[0], self.size[1] * self.screen_diff()[1])

        if _size[1] == 0: _size = (_size[0], self.surface.get_rect().height)
        if _size[0] == 0: _size = (self.surface.get_rect().width, _size[1])
        return _size
    
    def get_screen_size_resolution(self, size = None, resolution = 1):
        _size = self.get_screen_size(size)
        if _size[0] != 0: _size = self.get_screen_size_resolution_index(size, resolution, 0)
        if _size[1] != 0: _size = self.get_screen_size_resolution_index(size, resolution, 1)
        return _size
    
    def get_screen_size_resolution_index(self, size = None, resolution = 1, index: int = 0):

        _size = self.get_screen_size(size)
        _size = (
            _size[index] * resolution,
            _size[index]
        )
        return _size

    
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
        return child

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
