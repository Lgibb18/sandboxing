from Engine.Gui.imports import *
class window(control):

    class window_kwargs(control_kwargs):
        title_color: pg.Color

    __is_dragging : bool = False
    __is_clicking : bool = False
    __drag_offset : tuple[float, float] = (0, 0)
    def __init__(self, **kwargs: Unpack[window_kwargs]):
        super().__init__(**kwargs)
        self.color = pg.Color(51,63,60, 128)
        self.title_color = pg.Color(22,48,58, 128)
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        self.title_panel = self.add_child(control(color=self.title_color, size=(1, 30), stretchX=True, position=(0, 1.085)))
        self.set_color(self.color)
        sign_update(self.update)


    def is_dragging(self): return self.__is_dragging
    
    def update(self):
        if not pg.mouse.get_pressed(3)[0]:
            self.__is_dragging = False
            self.__is_clicking = False
        if type(self.parent) is not list: return
        if self.title_panel.is_clicked() and not self.__is_dragging and not self.__is_clicking:
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
