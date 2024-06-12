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
        for component in entity.components:
            if component.__class__.__name__ == "PhysicsComponent":
                self.rect.center = flipy(component.body.position)
                self.image = pg.transform.rotate(self.orig_image, math.degrees(component.body.angle))
                self.rect = self.image.get_rect(center=self.rect.center)
                if self.rect.y > 2000:
                    component.space.remove(component.body, component.shape)
                    self.kill()

