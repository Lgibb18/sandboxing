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
            stretchX=True,
            stretchY=True,
            parent=gui.tree
        )



Command = TestUICommand("test")