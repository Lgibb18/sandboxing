from Engine.Params.loop import *
from dataclasses import dataclass
@dataclass
class Runtime:
    """Every runtime vars"""
    grid_placing : bool = False
    
    @Update
    def update():pass

runtime = Runtime()