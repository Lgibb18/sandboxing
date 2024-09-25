import pymunk as pm
from Engine.Utilities.sprites import *
import Engine.Scripts.entities as entities
from Engine.Scripts.DefaultEntity import DefaultEntity

# Components
from Scripts.Components.SpriteComponent import *
from Scripts.Components.DraggableComponent import *
from Scripts.Components.KillOnBottomComponent import *
from Scripts.Components.OutlineComponent import *

class SmallTileStoneEntity(DefaultEntity):
    canBeInMenu = True
    def __init__(self):
        super().__init__()
        self.entity = Entity(
            id = "smallTileStone",
            name = "Small Tile Stone",
            components = [
                SpriteComponent(pg.image.load("Assets/Sprites/small_tile_stone.png"), LAYER_4_OBJECTS),
                PhysicsComponent(pm.Body.DYNAMIC),
                DraggableComponent(),
                KillOnBottomComponent(),
                OutlineComponent()
            ]
        )
        entities.all_entities[self.entity.id] = self


SmallTileStoneEntity()
