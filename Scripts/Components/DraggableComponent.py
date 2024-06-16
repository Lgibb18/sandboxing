import Scripts.Engine.entities
from Scripts.Engine.entity import *
from Scripts.Engine.component import *
from Scripts.Engine.utils import *
import pygame as pg
import Scripts.Engine.camera as camera
from Scripts.Components.PhysicsComponent import *
class DraggableComponent(Component):
    def __init__(self, velocity : bool = True):
        self.is_dragging = False
        self.mrel = (0,0)
        self.velocity = velocity
        self.offset = (0,0)

    def Start(self, entity: Entity):
        pass

    def Update(self, entity: Entity):
        if (collision_check(camera.mouse_pos(), entity.transform.position, entity.transform.scale) or self.is_dragging):
            for event in Scripts.Engine.events.event_list:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for entities in Scripts.Engine.entities.created_entities:
                            if(entity == entities):
                                self.offset = vec_diff(entity.transform.position, camera.mouse_pos())
                                self.is_dragging = True
                                break
                elif event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.is_dragging = False
        if self.is_dragging:
            entity.transform.position = vec_add(camera.mouse_pos(), self.offset)
            if (get_component(PhysicsComponent, entity)[0]):
                b: PhysicsComponent = get_component(PhysicsComponent, entity)[1]
                b.body.position = flipy(vec_add(camera.mouse_pos(), self.offset))
                if self.velocity:
                    b.shape.body.velocity = Vec2d(self.mrel[0] * 5, -self.mrel[1] * 5)
            self.mrel = camera.main.mouse_rel


