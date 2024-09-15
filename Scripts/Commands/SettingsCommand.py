import Engine.Scripts.commands as commands
from Engine.Scripts.settings import *
from Engine.Scripts.utils import convert
class SettingsCommand:
    def __init__(self, name):
        commands.all_commands[name] = self

    def process(self, args : list):
        if len(args) < 2:
            return "settings <name> <value>"
        attr = Settings.__getattribute__(args[0])
        if attr != None:
            Settings.__setattr__(args[0], convert(args[1]))


Command = SettingsCommand("settings")