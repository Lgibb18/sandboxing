import pymunk as pm
from Engine.Utilities.sprites import *
import Engine.Scripts.entities as entities
from Engine.Scripts.DefaultEntity import DefaultEntity

# Components
from Scripts.Components.SpriteComponent import *
from Scripts.Components.DraggableComponent import *
from Scripts.Components.GridComponent import *

class GridEntity(DefaultEntity):
    canBeInMenu = False
    def __init__(self):
        super().__init__()
        self.entity = Entity(
            id = "grid",
            name = "Grid",
            components = [
                SpriteComponent(pg.image.load("Assets/Sprites/Engine/grid.png"), LAYER_3_UNDER_OBJECTS, (105, 105), False),
                GridComponent()
            ]
        )
        entities.all_entities[self.entity.id] = self



GridEntity()
