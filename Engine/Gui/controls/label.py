from Engine.Gui.imports import *

class label(control):

    class text_kwargs(control_kwargs):
        text: str
        font: pg.font.Font

    def __init__(self, **kwargs: Unpack[text_kwargs]):
        super().__init__(**kwargs)
        self.text = "hello world"
        self.font = pg.font.Font("Assets/Fonts/Arco.ttf", 15)
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        sign_draw(self.draw)

    def draw(self):
        self.surface = self.font.render(self.text, True, self.color)
        rect = self.surface.get_rect()
        resolution = rect.width / rect.height
        self.set_size_dont_update_resolution((
            self.size[0],
            self.size[1]),
            rect.height / rect.width
            )
    