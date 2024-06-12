from Scripts.Engine.entity import *
from Scripts.Components.PhysicsComponent import *
from Scripts.Engine.sprites import *
import pygame as pg
import typing
class SpriteComponent(pg.sprite.Sprite, Component):
    def __init__(self, surface : pg.Surface, sprites : Sprites):
        self.surface = surface
        self.sprites = sprites

    def Start(self, entity: Entity):
        super().__init__()
        self.orig_image = self.surface.convert_alpha()
        self.orig_image = pg.transform.scale(self.orig_image, entity.transform.scale)
        self.image = self.orig_image
        self.rect = self.image.get_rect(center=entity.transform.position)
        self.sprites.all_sprites.add(self)


    def Update(self, entity: Entity):
        self.rect.center = entity.transform.position
        self.image = pg.transform.rotate(self.orig_image, entity.transform.rotation)
        self.rect = self.image.get_rect(center=self.rect.center)
        if self.rect.y > 2000:
            self.kill()

