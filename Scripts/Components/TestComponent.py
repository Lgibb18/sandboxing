from Scripts.Engine.entity import *
from Scripts.Engine.component import *


class TestComponent(Component):
    def __init__(self, randattribute):
        self.randAttribute = randattribute

    def start(self, entity: Entity):
        print("TestComponent Start")
        print(self.randAttribute)

    def update(self, entity: Entity):
        print("update")

