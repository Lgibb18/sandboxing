import Engine.Scripts.commands as commands
import Engine.Utilities.clock as clock
from Engine.Scripts.gui import *
from Engine.Gui.controls.window import *
from Engine.Gui.controls.button import *
from Engine.Gui.controls.label import *
from Engine.Utilities.logger import *
from Engine.Utilities.loop import *
import random
class TestUICommand2:
    def __init__(self, name):
        commands.all_commands[name] = self

    def process(self, args : list):
        self.window = window(
            position=(0, 0),
            size=(0.3, 0.5),
            stretchX=True,
            stretchY=True,
            parent=gui.tree
        )



Command = TestUICommand2("test2")