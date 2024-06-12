import Scripts.Engine.game
from Scripts.Engine.entity import *
from Scripts.Engine.component import *
from Scripts.Engine.utils import *
import pygame as pg
from Scripts.Components.PhysicsComponent import *
class DraggableComponent(Component):
    def __init__(self):
        self.is_dragging = False
        self.mrel = (0,0)

    def Start(self, entity: Entity):
        pass

    def Update(self, entity: Entity):
        if (collision_check(pg.mouse.get_pos(), entity.transform.position, entity.transform.scale) or self.is_dragging):
            for event in Scripts.Engine.events.event_list:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for entities in Scripts.Engine.game.all_entities:
                            if(entity == entities):
                                self.is_dragging = True
                                break
                elif event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.is_dragging = False
        if self.is_dragging:
            entity.transform.position = pg.mouse.get_pos()
            if (get_component(PhysicsComponent, entity)[0]):
                b: PhysicsComponent = get_component(PhysicsComponent, entity)[1]
                b.body.position = flipy(pg.mouse.get_pos())
                b.shape.body.velocity = Vec2d(self.mrel[0] * 5, -self.mrel[1] * 5)
                print(str(b.shape.body.velocity.x) + ", " + str(b.shape.body.velocity.y))
            self.mrel = pg.mouse.get_rel()


