import pygame as pg
class Camera:
    def __init__(self):
        self.pos = (0,0)

    def update(self):
        m = pg.mouse.get_rel()
        if pg.mouse.get_pressed(3)[1]:
            self.pos = (self.pos[0] + m[0], self.pos[1] + m[1])

def mouse_pos():
    m = pg.mouse.get_pos()
    return(m[0] - main.pos[0], m[1] - main.pos[1])

main = Camera()