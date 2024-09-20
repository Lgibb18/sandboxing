from Engine.Gui.imports import *

class label(control):

    class text_kwargs(control_kwargs):
        text: str
        font: str
        font_size : int
        max_x: int
        background_color : pg.Color

    def __init__(self, **kwargs: Unpack[text_kwargs]):
        super().__init__(**kwargs)
        self.text = "hello world"
        self.font_size = 15
        self.font = "Assets/Fonts/Arco.ttf"
        self.max_x = 0.3
        self.background_color = None
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        self.__font = pg.font.Font(self.font, self.font_size)
        sign_draw(self.draw)

    def draw(self):
        self.surface = self.__font.render(self.text, True, self.color, self.background_color)
