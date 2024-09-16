import time

import Engine.Scripts.sprites
from Engine.Scripts.events import *
from Engine.Scripts.console import *
from Engine.Scripts.inventory import *
from Engine.Scripts.entities import *
from pymunk import Vec2d
import pymunk as pm
import Engine.Scripts.clock as clock
from Engine.Scripts.settings import *
from pygame.locals import *
space = pm.Space()

class Game:
    def __init__(self):
        pg.init()
        self.resolution = (1280, 720)
        flags = DOUBLEBUF | pg.RESIZABLE
        self.screen = pg.display.set_mode(self.resolution, flags)
        icon = pg.image.load("Assets/Sprites/db.png")
        pg.display.set_icon(icon)
        pg.display.set_caption('Nighty box 2', 'nb2')


        self.sprites = Sprites(self.screen)
        Engine.Scripts.sprites.every_sprites = self.sprites
        self.console = Console(self.screen)
        self.inventory = Inventory(self.screen)


        self.done = False
        self.clock = pg.time.Clock()
        clock.main_clock = self.clock

        space.gravity = Vec2d(0.0, -900.0)
        space.damping = .9

        Instantiate("map", Transform((self.resolution[0] / 2,self.resolution[1]), (self.resolution[0]*50, 100)))

        self.dt = 0
        self.current_fps = 0

    def run(self):
        while not self.done:
            self.dt = self.clock.tick(clock.target_fps) / 1000
            camera.main.update()
            self.run_logic()
            self.draw()
            self.handle_events()
            self.current_fps = self.clock.get_fps()
            events.keyboard_list.clear()

        pg.quit()


    def handle_events(self):
        Events()
        self.console.update()
        self.inventory.update()
        for event in events.event_list:
            if event.type == pg.QUIT:
                self.done = True




    def run_logic(self):
        if self.current_fps > 0:
            steps = Settings.steps
            for i in range(0,steps):
                space.step((1*self.dt/steps))
        entities_update()
        self.sprites.run_logic()

    def draw(self):
        self.screen.fill(pg.Color(134, 183, 181))
        self.sprites.draw()
        self.inventory.draw()
        self.console.draw()
        pg.display.update()

