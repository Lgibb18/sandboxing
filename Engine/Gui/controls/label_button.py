from Engine.Gui.imports import *
from Engine.Gui.controls.button import *
from Engine.Gui.controls.label import *
class label_button(control):
    class label_button_kwargs(label.text_kwargs, button.button_kwargs):
        pass

    def __init__(self, **kwargs: Unpack[label_button_kwargs]):
        super().__init__(**kwargs)
        sign_update(self.update)
        sign_draw(self.draw)
        self.on_click = lambda : 0
        self.on_click_args = None
        self.clicked_color = pg.Color(200,200,200,255)
        self.normal_color = self.color
        self.hovered_color = pg.Color(240,240,240,255)
        self.text = "hello world"
        self.font_size = 15
        self.font = "Assets/Fonts/Arco.ttf"
        self.max_x = 0.3
        self.background_color = None
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        self.__font = pg.font.Font(self.font, self.font_size)

    def draw(self):
        self.surface = self.__font.render(self.text, True, self.color, self.background_color)

    def update(self):
        if(self.on_clicked(True)):
            self.set_size((100,100))
            if self.on_click_args != None:
                self.on_click(self.on_click_args)
            else:
                self.on_click()
        if(self.is_clicked(True)):
            self.color = self.clicked_color
        else:
            if(self.is_hovered(True)):
                self.color = self.hovered_color
            else:
                self.color = self.normal_color

        