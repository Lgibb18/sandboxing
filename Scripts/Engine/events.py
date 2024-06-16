import pygame as pg
import Scripts.Engine
event_list = []
keyboard_event = None
keyboard_list = []
from Scripts.Engine.entities import *
import Scripts.Engine.camera as camera
class Events:
    def __init__(self):
        self.handle_events()

    def handle_events(self):
            Scripts.Engine.events.event_list = pg.event.get()
            for event in Scripts.Engine.events.event_list:
                if event.type == pg.KEYDOWN:
                    Scripts.Engine.events.keyboard_event = event
                    keyboard_list.append(event.key)

            for key in Scripts.Engine.events.keyboard_list:
               if key == pg.K_e:
                Instantiate("planks", Transform(camera.mouse_pos()))
