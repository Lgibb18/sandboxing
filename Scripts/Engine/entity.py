import pygame as pg
import pymunk as pm
from pymunk import Vec2d
import pymunk.pygame_util
from Scripts.Engine.utils import *
import importlib.util
class Transform:
    position : tuple[int, int] = (0,0)
    scale : tuple[float, float] = (50,50)
    rotation : float = 0
    isUI : bool = False

    def __init__(self, position : tuple[int, int] = (0, 0), scale : tuple[float, float] = (50,50), rotation : float = 0):
        self.position = position
        self.scale = scale
        self.rotation = rotation

class Entity:
    name: str = None
    transform : Transform = None
    components : list[classmethod] = None

    m = importlib.util.spec_from_file_location("Component", "/component.py")
    def __init__(self,
                 name: str = "Object",
                 transform: Transform = Transform(),
                 components: list[m] = []
                 ):
        super().__init__()
        self.name = name
        self.transform = transform
        self.components = components
        for component in components:
            if component.active:
                component.Start(self)


    def update(self):
        for component in self.components:
            if component.active:
                component.Update(self)
