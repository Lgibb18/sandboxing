import Scripts.Engine.commands as commands
import Scripts.Engine.sprites as sprites
class SetLayerVisibilityCommand:
    def __init__(self, name):
        commands.all_commands[name] = self

    def process(self, args : list):
        if len(args) < 2:
            return "setlayervisibility{layer} {boolean}"

        if str(args[0]).isalnum():
            num = int(args[0])
        else:
            return "layer is not number"

        if num not in range(0,8):
            return "layer not in range(0,8)"

        if str(args[1]).lower() == "true":
            if num in sprites.disabled_layers:
                sprites.disabled_layers.remove(num)
        elif str(args[1 ]).lower() == "false":
            if num not in sprites.disabled_layers:
                sprites.disabled_layers.append(num)
        else:
            return "boolean is not boolean"


        return ""



Command = SetLayerVisibilityCommand("setlayervisibility")