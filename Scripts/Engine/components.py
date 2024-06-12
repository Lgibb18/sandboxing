from Scripts.Engine.entity import *
from Scripts.Engine.component import *


def get_component(component : Component, entity : Entity):
    for componen in entity.components:
        if componen.__class__.__name__ == component.__class__.__name__:
            return True, componen
    return False, None

