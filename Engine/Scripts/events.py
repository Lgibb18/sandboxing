import pygame as pg
import Engine

event_list : list[pg.event.Event] = []
keyboard_event = None
keyboard_list = []

class Events:
    def __init__(self):
        pg.key.set_repeat(500,100)
        self.handle_events()

    def handle_events(self):
            Engine.Scripts.events.event_list = pg.event.get()
            for event in Engine.Scripts.events.event_list:
                if event.type == pg.KEYDOWN:
                    Engine.Scripts.events.keyboard_event = event
                    keyboard_list.append((event, event.key))

