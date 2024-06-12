from Scripts.Engine.entity import *


class Component:
    active = True
    def __init__(self):
        pass

    def Start(self, entity: Entity):
        pass

    def Update(self, entity: Entity):
        pass

def get_component(component, entity : Entity):
    if entity is not None:
        for componen in entity.components:
            if componen.__class__.__name__ == component.__name__:
                return True, componen
        return False, None
    else:
        return False, None