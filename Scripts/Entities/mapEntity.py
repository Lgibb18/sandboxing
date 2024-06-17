import pymunk as pm
from Engine.Scripts.sprites import *
import Engine.Scripts.entities as entities

# Components
from Scripts.Components.SpriteComponent import *
from Scripts.Components.DraggableComponent import *


class MapEntity:
    canBeInMenu = False
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    def __init__(self):
        self.entity = Entity(
            id = "map",
            name = "Map",
            components = [
                SpriteComponent(pg.image.load("Engine/Sprites/white.png"), LAYER_1_GROUND),
                PhysicsComponent(pm.Body.STATIC),
            ]
        )
        entities.all_entities[self.entity.id] = self


    def instantiate(self, transform: Transform):
        sef = MapEntity()
        sef.entity.instantiate(transform)
        entities.created_entities.append(sef.entity)


MapEntity()
