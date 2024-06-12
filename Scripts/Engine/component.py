from Scripts.Engine.entity import *


class Component:
    active = True
    def __init__(self):
        pass

    def Start(self, entity: Entity):
        pass

    def Update(self, entity: Entity):
        print(1)
        pass

def get_component(component, entity : Entity):
    for componen in entity.components:
        if componen.__class__.__name__ == component.__name__:
            return True, componen
    return False, None