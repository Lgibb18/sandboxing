import Engine.Scripts.commands as commands
from Engine.Scripts.entities import *
import Engine.Scripts.camera as camera
class InstantiateCommand:
    def __init__(self, name):
        commands.all_commands[name] = self

    def process(self, args : list):
        if len(args) < 3:
            return "instantiate <id> <x> <y>"
        try:
            x = int(args[1])
        except:
            if args[1] == "-":
                x = camera.mouse_pos()[0]
            else:
                return "x is not number"
        try:
            y = int(args[2])
        except:
            if args[2] == "-":
                y = camera.mouse_pos()[1]
            else:
                return "y is not number"
        if args[0] not in list(all_entities.keys()):
            return f"{args[0]} doesn't exist"
        Instantiate(args[0], Transform((x, y)))





Command = InstantiateCommand("instantiate")