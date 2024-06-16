import Scripts.Engine.commands as commands
from Scripts.Engine.entities import *
import Scripts.Engine.camera as camera
class PosCommand:
    def __init__(self, name):
        commands.all_commands[name] = self

    def process(self, args : list):
        return str(camera.mouse_pos())





Command = PosCommand("pos")