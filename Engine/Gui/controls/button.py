from Engine.Gui.imports import *

class button(control):

    class button_kwargs(control_kwargs):
        on_click: object
        on_click_args: object
        clicked_color: pg.Color
        normal_color: pg.Color

    def __init__(self, **kwargs: Unpack[button_kwargs]):
        super().__init__(**kwargs)
        sign_update(self.update)
        self.on_click = None
        self.on_click_args = None
        self.clicked_color = pg.Color(200,200,200,255)
        self.normal_color = self.color
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def update(self):
        if(self.on_clicked()):
            self.set_size((100,100))
            if self.on_click_args != None:
                self.on_click(self.on_click_args)
            else:
                self.on_click()
        if(self.is_clicked()):
            self.set_color(self.clicked_color)
        else:
            self.set_color(self.normal_color)

    