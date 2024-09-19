import Engine.Scripts.commands as commands
import Engine.Utilities.clock as clock
from Engine.Scripts.gui import *
from Engine.Gui.controls.window import *
from Engine.Gui.controls.button import *
from Engine.Gui.controls.label import *
from Engine.Utilities.logger import *
from Engine.Utilities.loop import *
import random
class TestUICommand:
    def __init__(self, name):
        commands.all_commands[name] = self

    def process(self, args : list):
        self.window = window(
            position=(-random.random()+random.random(),-random.random()+random.random()),
            size=(0.3, 0.5),
            stretch=True,
            parent=gui.tree
        )
        self.button = button(
            size=(0.3, 0.3),
            position=(0, 0.5),
            stretch=True,
            parent=self.window
        )
        self.button2 = button(
            size=(0.3, 0.3),
            on_click=self.window.destroy,
            position=(0, -0.5),
            stretch=True,
            parent=self.window
        )
        self.label = label(
            stretch=True,
            size=(1,1),
            position=(0,0),
            text="shimmy, shimmy ya",
            parent=self.window
        )
        self.button.on_click = self.button.destroy
        self.window.set_color(pg.Color(random.randint(0,255), random.randint(0,255), random.randint(0,255), 255))




Command = TestUICommand("test")