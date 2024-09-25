from Engine.Utilities.sprites import *
import Engine.Scripts.entities as entities
import pymunk as pm
from Engine.Scripts.DefaultEntity import DefaultEntity

# Components
from Scripts.Components.SpriteComponent import *
from Scripts.Components.DraggableComponent import *
from Scripts.Components.KillOnBottomComponent import *
from Scripts.Components.OutlineComponent import *

class StoneEntity(DefaultEntity):
    canBeInMenu = True
    def __init__(self):
        super().__init__()
        self.entity = Entity(
            id = "stone",
            name = "Stone",
            components = [
                SpriteComponent(pg.image.load("Assets/Sprites/stone.png"), LAYER_4_OBJECTS),
                PhysicsComponent(pm.Body.DYNAMIC),
                DraggableComponent(),
                KillOnBottomComponent(),
                OutlineComponent()
            ]
        )
        entities.all_entities[self.entity.id] = self


StoneEntity()
