import pygame as pg
import Scripts.Engine
event_list = []
class Events:
    def __init__(self):
        self.handle_events()

    def handle_events(self):
            Scripts.Engine.events.event_list = pg.event.get()