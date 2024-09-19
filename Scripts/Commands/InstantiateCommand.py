import Engine.Scripts.commands as commands
from Engine.Scripts.entities import *
import Engine.Scripts.camera as camera
from Engine.Utilities.utils import convert
class InstantiateCommand:
    def __init__(self, name):
        commands.all_commands[name] = self

    def process(self, args : list):
        if len(args) < 3:
            return "instantiate <id> <x> <y> <count>"
        
        # x position
        if(convert.type(args[1]) is int):
            x = int(args[1])
        else:
            if args[1] == "m":
                x = camera.mouse_pos()[0]
            else: return "x is not position"

        # y position
        if(convert.type(args[2]) is int):
            y = int(args[2])
        else:
            if args[2] == "m":
                y = camera.mouse_pos()[1]
            else: return "y is not position"

        # entity
        if args[0] not in list(all_entities.keys()):
            return f"{args[0]} does not exist"

        # count        
        if(len(args) >= 4 and convert.type(args[3]) is int):
            for i in range(int(args[3])):
                Instantiate(args[0], Transform((x, y + i)))
            return        

        Instantiate(args[0], Transform((x, y)))





Command = InstantiateCommand("instantiate")