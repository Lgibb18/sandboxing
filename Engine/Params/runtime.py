from Engine.Params.loop import *
from dataclasses import dataclass
from Engine.Scripts.events import *
from Engine.Utilities.logger import *
@dataclass
class Runtime:
    """Every runtime vars"""
    grid_placing : bool = False

runtime = Runtime()

@Update
def update():
    for (event, key) in keyboard_list:
        if key == pg.K_g:
            runtime.grid_placing = not runtime.grid_placing
            debug(runtime.grid_placing)
            