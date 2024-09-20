from Engine.Gui.controls.control import *
from typing_extensions import Unpack, TypedDict
from Engine.Utilities.logger import *
import pygame as pg
from Engine.Utilities.loop import *
from Engine.Scripts.events import *
from Engine.Utilities.utils import *
from Engine.Utilities.gui_tools import *

def diff_from_standart_resolution():
    size = pg.display.get_window_size()
    return (
        size[0] / 1280,
        size[1] / 720
    )

def diff_from_standart_resolution_one():
    size = pg.display.get_window_size()
    return (size[0] / 1280) * (size[1] / 720)