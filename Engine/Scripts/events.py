import pygame as pg
import Engine
from Engine.Utilities.manager import *

event_list : list[pg.event.Event] = []
keyboard_event = None
keyboard_list = []
is_downed : bool = False


class Events:
    def __init__(self):
        pg.key.set_repeat(500,100)
        self.handle_events()

    def handle_events(self):
            if not Engine.Scripts.events.is_downed and pg.mouse.get_pressed():
                 Engine.Scripts.events.is_downed = True
            else:
                 Engine.Scripts.events.is_downed = False
            Engine.Scripts.events.event_list = pg.event.get()
            for event in Engine.Scripts.events.event_list:
                if event.type == pg.KEYDOWN:
                    Engine.Scripts.events.keyboard_event = event
                    keyboard_list.append((event, event.key))
                if event.type == pg.VIDEORESIZE:
                    manager.manager.set_window_resolution((event.w, event.h))

