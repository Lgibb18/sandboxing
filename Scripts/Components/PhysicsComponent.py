from Scripts.Engine.entity import *
from Scripts.Engine.component import *
from Scripts.Engine.utils import *
import Scripts.Engine.game as game
class PhysicsComponent(Component):
    def __init__(self, bodyType: int = pm.Body.DYNAMIC, mass: float = 1, friction: float = .99,
                 elasticity: float = 0):
        self.space = game.space
        self.bodyType = bodyType
        self.mass = mass
        self.friction = friction
        self.elasticity = elasticity

    def Start(self, entity: Entity):
        entity.transform.position = flipy(entity.transform.position)
        moment = pm.moment_for_box(self.mass, (entity.transform.scale[0], entity.transform.scale[1]))
        self.body = pm.Body(self.mass, moment, self.bodyType)
        self.shape = pm.Poly.create_box(self.body, entity.transform.scale)
        self.shape.friction = self.friction
        self.shape.elasticity = self.elasticity
        self.body.position = entity.transform.position
        self.space = self.space
        self.space.add(self.body, self.shape)
        entity.transform.position = flipy(self.body.position)
        entity.transform.rotation = math.degrees(self.body.angle)
    def Update(self, entity: Entity):
        entity.transform.position = flipy(self.body.position)
        entity.transform.rotation = math.degrees(self.body.angle)
        if entity.transform.position[1] > 2000:
            try:
                self.space.remove(self.body, self.shape)
            except: pass