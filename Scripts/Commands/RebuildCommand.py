import Engine.Scripts.commands as commands
from Engine.Utilities.logger import *
from Engine.Params.classes import classes
class RebuildCommand:
    def __init__(self, name):
        commands.all_commands[name] = self
        debug(commands.all_commands)

    def process(self, args : list):
        classes.inventory.rebuild()


Command = RebuildCommand("rebuild")