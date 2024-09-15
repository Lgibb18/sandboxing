import Engine.Scripts.commands as commands
import Engine.Scripts.clock as clock
class SetFpsCommand:
    def __init__(self, name):
        commands.all_commands[name] = self

    def process(self, args : list):
        if len(args) < 1:
            return "setfps <fps>"
        if not str(args[0]).isalnum():
            return "setfps <fps> must be alphanumeric"
        fps = int(args[0])
        if not fps in range(10, 1001):
            return "setfps <fps> not in range(10,1000)"
        clock.target_fps = fps


Command = SetFpsCommand("setfps")