from Scripts.Engine.entity import *
from Scripts.Engine.component import *
from Scripts.Engine.utils import *

class PhysicsComponent(Component):
    def __init__(self, space: pm.Space, bodyType: int = pm.Body.DYNAMIC, mass: float = 1, friction: float = .99,
                 elasticity: float = 0):
        self.space = space
        self.bodyType = bodyType
        self.mass = mass
        self.friction = friction
        self.elasticity = elasticity

    def start(self, entity: Entity):
        entity.transform.position = flipy(entity.transform.position)
        moment = pm.moment_for_box(self.mass, (entity.transform.scale[0], entity.transform.scale[1]))
        self.body = pm.Body(self.mass, moment, self.bodyType)
        self.shape = pm.Poly.create_box(self.body, entity.transform.scale)
        self.shape.friction = self.friction
        self.shape.elasticity = self.elasticity
        self.body.position = entity.transform.position
        self.space = self.space
        self.space.add(self.body, self.shape)
    def update(self, entity: Entity):
        entity.rect.center = flipy(self.body.position)
        entity.image = pg.transform.rotate(entity.orig_image, math.degrees(self.body.angle))
        entity.rect = entity.image.get_rect(center=entity.rect.center)
        if entity.rect.y > 2000:
            self.space.remove(self.body, self.shape)
            entity.kill()
