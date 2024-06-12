import pygame as pg
import Scripts.Engine.camera as camera
class Camera:
    def __init__(self):
        self.pos = (0,0)
        self.mouse_rel = (0,0)

    def update(self):
        self.mouse_rel = camera.mouse_rel()
        if pg.mouse.get_pressed(3)[1]:
            self.pos = (self.pos[0] + self.mouse_rel[0], self.pos[1] + self.mouse_rel[1])

def mouse_pos():
    m = pg.mouse.get_pos()
    return(m[0] - main.pos[0], m[1] - main.pos[1])

def mouse_rel():
    return pg.mouse.get_rel()


main = Camera()