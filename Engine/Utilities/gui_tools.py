import pygame as pg
class tools:
    def __init__(self) -> None:
        pass

    def screen_to_ui(self, pos: tuple[int, int]):
        resolution = pg.display.get_window_size()
        position = (
             ((pos[0] / (resolution[0])) - 0.5) * 2,
            -((pos[1] / (resolution[1])) - 0.5) * 2
        )
        return position
    
gui_tools = tools()