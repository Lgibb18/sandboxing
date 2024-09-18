import Engine.Scripts.commands as commands
import Engine.Utilities.clock as clock
class FpsCommand:
    def __init__(self, name):
        commands.all_commands[name] = self

    def process(self, args : list):
        if clock.main_clock != None:
            return clock.main_clock


Command = FpsCommand("fps")