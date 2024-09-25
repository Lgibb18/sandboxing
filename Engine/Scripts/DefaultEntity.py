import pymunk as pm
from Engine.Utilities.sprites import *
import Engine.Scripts.entities as entities
from Engine.Scripts.entity import *

class DefaultEntity:
    canBeInMenu = True
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    def __init__(self):
        self.entity = Entity(
            id="default",
            name="Default"
        )
        entities.all_entities[self.entity.id] = self

    def instantiate(self, transform: Transform):
        sef = self.__class__()
        sef.entity.instantiate(transform)
        return sef.entity