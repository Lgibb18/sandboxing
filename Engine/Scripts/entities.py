from Engine.Scripts.entity import *
from Engine.Params.loop import *
all_entities: dict = {}
created_entities : list[Entity] = []


def Instantiate(id : str, transform : Transform):
    all_entities[id].instantiate(transform)

@Logic
def entities_update():
    for i in created_entities:
        i.update()

