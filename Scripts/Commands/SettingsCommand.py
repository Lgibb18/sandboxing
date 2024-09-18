import Engine.Scripts.commands as commands
from Engine.Utilities.settings import *
from Engine.Utilities.utils import convert
class SettingsCommand:
    def __init__(self, name):
        commands.all_commands[name] = self

    def process(self, args : list):
        if len(args) < 2:
            return "settings <name> <value>"
        try:
            attr = Settings.__getattribute__(args[0])
            Settings.__setattr__(args[0], convert(args[1]))
            Settings.save()
        except AttributeError as e:
            return f"setting {args[0]} not found"


Command = SettingsCommand("settings")