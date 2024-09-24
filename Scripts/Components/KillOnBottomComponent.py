from Scripts.Components.PhysicsComponent import *
from Scripts.Components.SpriteComponent import *
class KillOnBottomComponent(Component):
    def Update(self, entity: Entity):
        if entity.transform.position[1] > 2000:
            returned, comp = get_component(SpriteComponent,entity)
            if returned:
                comp.kill()
            returned, comp = get_component(PhysicsComponent, entity)
            if returned:
                try:
                    comp.space.remove(comp.body, comp.shape)
                except: pass
                
                
            

