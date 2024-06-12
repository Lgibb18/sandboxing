import pygame as pg
import pymunk as pm
from pymunk import Vec2d
import pymunk.pygame_util
from Scripts.Engine.utils import *
import importlib.util
class Transform:
    position : tuple[int, int] = (0,0)
    scale : tuple[float, float] = (50,50)
    isUI : bool = False

    def __init__(self, position : tuple[int, int] = (0, 0), scale : tuple[float, float] = (50,50)):
        self.position = position
        self.scale = scale

class Entity(pg.sprite.Sprite):
    surface : pg.Surface = None
    name: str = None
    transform : Transform = None
    components : list[classmethod] = None

    m = importlib.util.spec_from_file_location("Component", "/component.py")
    def __init__(self,
                 surface: pg.Surface,
                 name: str = "Object",
                 transform: Transform = Transform(),
                 components: list[m] = []
                 ):
        super().__init__()
        self.surface = surface
        self.name = name
        self.transform = transform
        self.components = components
        # Object
        self.orig_image = surface.convert_alpha()
        self.orig_image = pg.transform.scale(self.orig_image, transform.scale)
        self.image = self.orig_image
        self.rect = self.image.get_rect(center=transform.position)
        for component in components:
            component.start(self)


    def update(self):
        for component in self.components:
            component.update(self)
