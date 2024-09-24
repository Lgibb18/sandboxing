import pymunk as pm
from Engine.Utilities.sprites import *
import Engine.Scripts.entities as entities
from Engine.Scripts.DefaultEntity import DefaultEntity

# Components
from Scripts.Components.SpriteComponent import *
from Scripts.Components.DraggableComponent import *
from Scripts.Components.KillOnBottomComponent import *

class MapEntity(DefaultEntity):
    canBeInMenu = False
    def __init__(self):
        super().__init__()
        self.entity = Entity(
            id = "map",
            name = "Map",
            components = [
                SpriteComponent(pg.image.load("Assets/Sprites/Engine/white.png"), LAYER_4_OBJECTS),
                PhysicsComponent(pm.Body.STATIC),
                KillOnBottomComponent()
            ]
        )
        entities.all_entities[self.entity.id] = self


MapEntity()
