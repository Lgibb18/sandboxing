import pygame as pg
import pymunk as pm
from Scripts.Engine.entity import *
from Scripts.Engine.entities import *
from Scripts.Engine.sprites import *
import Scripts.Engine.entities as entities

# Components
from Scripts.Components.SpriteComponent import *
from Scripts.Components.PhysicsComponent import *
from Scripts.Components.DraggableComponent import *


class StoneEntity:
    canBeInMenu = True
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    def __init__(self):
        self.entity = Entity(
            id = "stone",
            name = "Stone",
            components = [
                SpriteComponent(pg.image.load("Sprites/stone.png"), LAYER_4_OBJECTS),
                PhysicsComponent(pm.Body.DYNAMIC),
                DraggableComponent()
            ]
        )
        entities.all_entities[self.entity.id] = self

    def instantiate(self, transform: Transform):
        sef = StoneEntity()
        sef.entity.instantiate(transform)
        entities.created_entities.append(sef.entity)


StoneEntity()
