import pymunk as pm
from Engine.Utilities.sprites import *
import Engine.Scripts.entities as entities

# Components
from Scripts.Components.SpriteComponent import *
from Scripts.Components.DraggableComponent import *


class StoneBricksEntity:
    canBeInMenu = True
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    def __init__(self):
        self.entity = Entity(
            id = "stoneBricks",
            name = "Stone Bricks",
            components = [
                SpriteComponent(pg.image.load("Assets/Sprites/stone_bricks.png"), LAYER_4_OBJECTS),
                PhysicsComponent(pm.Body.DYNAMIC),
                DraggableComponent()
            ]
        )
        entities.all_entities[self.entity.id] = self

    def instantiate(self, transform: Transform):
        sef = self.__class__()
        sef.entity.instantiate(transform)
        entities.created_entities.append(sef.entity)


StoneBricksEntity()
