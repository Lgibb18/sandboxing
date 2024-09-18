from Scripts.Components.PhysicsComponent import *
import pygame as pg
import Engine.Utilities.sprites as sprites


class SpriteComponent(pg.sprite.Sprite, Component):
    def __init__(self, surface : pg.Surface, spriteLayer: int = 4, scale: tuple[float, float] = (1,1)):
        self.spriteLayer = spriteLayer
        self.surface = surface
        self.scale = scale
        if(spriteLayer > 8 or spriteLayer < 0):
            raise Exception(f"layer {spriteLayer} not in range (0,8)")

    def Start(self, entity: Entity):
        super().__init__()
        self.orig_image = self.surface.convert_alpha()
        self.orig_image = pg.transform.scale(self.orig_image, (entity.transform.scale[0] * self.scale[0], entity.transform.scale[1] * self.scale[1]))
        self.image = self.orig_image
        self.rect = self.image.get_rect(center=entity.transform.position)
        sprites.every_sprites.all_sprites[self.spriteLayer].add(self)


    def Update(self, entity: Entity):
        self.rect.center = entity.transform.position
        self.image = pg.transform.rotate(self.orig_image, entity.transform.rotation)
        self.rect = self.image.get_rect(center=self.rect.center)
        if entity.transform.position[1] > 2000:
            self.kill()

