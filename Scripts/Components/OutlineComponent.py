from Scripts.Components.SpriteComponent import *
import pygame as pg
import Engine.Utilities.sprites as sprites
from Engine.Params.settings import *
import Engine.Scripts.camera as camera
class OutlineComponent(Component):
    def __init__(self, width: int = 3, color = (0,255,0), quality : int = 2, only_on_mouse : bool = True):
        self.spriteComp : SpriteComponent | None = None
        self.width = width
        self.color = color
        self.quality = quality
        self.only_on_mouse = only_on_mouse

    def draw_outline(self, entity: Entity, image : pg.Surface,color=(0,0,0), width: int = 3):
        rect = image.get_rect()
        mask = pg.mask.from_surface(image)
        outline = mask.outline(self.quality)
        outline_image = pg.Surface(rect.size).convert_alpha()
        outline_image.fill((0,0,0,0))
        points = []
        for point in outline:
            points.append(point)
        pg.draw.lines(outline_image, color, True, points, width)
        sprites.blit_layer_camera(outline_image, entity.transform.position, sprites.LAYER_5_OVER_OBJECTS)

    def Start(self, entity: Entity):
        for comp in entity.components:
            if type(comp) == SpriteComponent:
                self.spriteComp = comp
        if self.spriteComp == None:
            error(f"No SpriteComponent, but OutlineComponent on entity {entity.id}")
            self.Kill(entity)

    def Update(self, entity: Entity):
        if self.spriteComp == None: return
        if collision_check(camera.mouse_pos(), entity.transform.position, entity.transform.scale) or not self.only_on_mouse:
            self.draw_outline(entity, self.spriteComp.image, self.color, self.width)
