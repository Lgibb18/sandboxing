import importlib.util
import pygame as pg


class Transform:
    __prev_rotation : float = 0
    position : tuple[int, int] = (0,0)
    scale : tuple[float, float] = (50,50)
    rotation : float = 0
    isUI : bool = False

    def __init__(self, position : tuple[int, int] = (0, 0), scale : tuple[float, float] = (50,50), rotation : float = 0):
        self.position = position
        self.scale = scale
        self.rotation = rotation

    def set_rotation(self, angle : float):
        self.__prev_rotation = self.rotation
        self.rotation = angle

    def get_prev_rotation(self) -> float:
        return self.__prev_rotation


class Entity:
    id: str = None
    name: str = None
    transform : Transform = None
    components : list[classmethod] = None
    icon : pg.Surface = None
    created : bool = False

    m = importlib.util.spec_from_file_location("Component", "component.py")
    def __init__(self,
                 id: str,
                 name: str = "Object",
                 components: list[m] = [],
                 icon : pg.Surface = None
                 ):
        self.id = id
        self.name = name
        self.components = components
        self.icon = icon
        if icon == None:
            for comp in self.components:
                if comp.__class__.__name__ == "SpriteComponent":
                    self.icon = comp.surface



    def instantiate(self, transform : Transform = Transform()):
        self.transform = transform
        self.created = True
        for component in self.components:
            if component.active:
                component.Start(self)
    def update(self):
        if self.created:
            for component in self.components:
                if component.active:
                    component.Update(self)
