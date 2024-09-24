import Engine.Scripts.entities
import Engine.Scripts.camera as camera
from Scripts.Components.PhysicsComponent import *
import Engine.Scripts.events as events
class GridComponent(Component):
    def Update(self, entity: Entity):
        reso = pg.display.get_window_size()
        entity.transform.position = (
            (-camera.main.pos[0] + reso[0] / 2) // 50 * 50,
            (-camera.main.pos[1] + reso[1] / 2) // 50 * 50
        )