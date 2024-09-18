from Engine.Gui.controls.control import *
from Engine.Utilities.sprites import *
from Engine.Utilities.loop import *
from Engine.Utilities.logger import *
class Gui:
    def __init__(self) -> None:
        sign_draw(self.draw)
        self.tree = []

    def draw(self):
        for control in self.tree:
                self.render_control(control)

    def __render_control(self, control : control):
        position = control.get_screen_pos()
        blit_layer(control.surface, position, LAYER_7_UI)

    def render_control(self, control : control):
        if control.visible:
            self.__render_control(control)
            for i in control.children:
                self.render_control(i)

gui = Gui()