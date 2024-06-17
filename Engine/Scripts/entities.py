import Engine.Scripts.entities
from Engine.Scripts.entity import *
all_entities: dict = {}
created_entities : list[Entity] = []


def Instantiate(id : str, transform : Transform):
    all_entities[id].instantiate(transform)

def entities_update():
    for i in created_entities:
        i.update()
