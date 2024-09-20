from Engine.Gui.imports import *
from Engine.Gui.controls.label import *
from Engine.Gui.controls.label_button import *
class window(control):

    class window_kwargs(control_kwargs):
        title_color: pg.Color
        title: str

    __is_dragging : bool = False
    __is_clicking : bool = False
    __drag_offset : tuple[float, float] = (0, 0)
    def __init__(self, **kwargs: Unpack[window_kwargs]):
        super().__init__(**kwargs)
        self.color = pg.Color(51,63,60, 128)
        self.title_color = pg.Color(22,48,58, 128)
        self.title = "Window"
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        self.title_panel = self.add_child(control(color=self.title_color, size=(1, 30), stretchX=True, position=(0, 1.07)))
        self.title_panel.add_child(label(text="window", size=(0.98, 25), stretchX=True, font_size=25))
        self.crutch = self.title_panel.add_child(control(name="crutch", size=(30, 30), position=(0.5, 0), color=pg.Color(0,0,0,128)))
        self.crutch.add_child(label_button(text="X", size=(0, 25), position=(0, 0), font_size=25, on_click=self.destroy))
        self.set_color(self.color)
        sign_update(self.update)

    def is_dragging(self): return self.__is_dragging
    
    def update(self):
        if not pg.mouse.get_pressed(3)[0]:
            self.__is_dragging = False
            self.__is_clicking = False
        if type(self.parent) is not list: return
        if self.is_clicked() and not self.__is_dragging and not self.__is_clicking:
                rtrn = False
                for control in self.parent[self.parent.index(self):]:
                     if control is self: continue
                     if isinstance(control, window): 
                          if control.is_dragging() or control.get_rect().collidepoint(pg.mouse.get_pos()):
                               rtrn = True
                               break
                if rtrn: return   
                          
                          
                pos = gui_tools.screen_to_ui(pg.mouse.get_pos())
                self.__drag_offset = (
                    pos[0] - self.position[0],
                    pos[1] - self.position[1]
                    )
                self.__is_dragging = True
                if type(self.parent) is list:
                     self.parent.append(self.parent.pop(self.parent.index(self)))
        if pg.mouse.get_pressed(3)[0]: self.__is_clicking = True
        if self.__is_dragging: 
            pos = gui_tools.screen_to_ui(pg.mouse.get_pos())
            self.position = (
                pos[0] - self.__drag_offset[0],
                pos[1] - self.__drag_offset[1]
            )
