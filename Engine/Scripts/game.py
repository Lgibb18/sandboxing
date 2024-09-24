import Engine.Utilities
import Engine.Utilities.sprites
from Engine.Scripts.events import *
from Engine.Scripts.console import *
from Scripts.Gui.inventory import *
from Engine.Scripts.entities import *
from pymunk import Vec2d
import pymunk as pm
import Engine.Utilities.clock as clock
from Engine.Params.settings import *
from Engine.Utilities.logger import *
from Engine.Params.loop import *
import pygame_gui
from Engine.Params.manager import *
import Engine.Params.runtime as rn
space = pm.Space()
from Engine.Params.classes import classes
class Game:
    def __init__(self):
        info("Hello, world!")        
        pg.init()
        self.resolution = (1280, 720)
        flags = pg.DOUBLEBUF | pg.RESIZABLE
        self.screen = pg.display.set_mode(self.resolution, flags)
        manager.manager = pygame_gui.UIManager(self.resolution, theme_path="Assets/Settings/ui_theme.json")

        icon = pg.image.load("Assets/Sprites/db.png")
        pg.display.set_icon(icon) 
        pg.display.set_caption('Nighty box 2', 'nb2')

        self.sprites = Sprites(self.screen)
        Engine.Utilities.sprites.every_sprites = self.sprites
        classes.console = Console(self.screen)
        classes.inventory = Inventory()
        self.done = False
        self.clock = pg.time.Clock()
        clock.main_clock = self.clock

        space.gravity = Vec2d(0.0, -900.0)
        space.damping = .9
        

        Instantiate("map", Transform((self.resolution[0] / 2,self.resolution[1]+5), (self.resolution[0]*50, 100)))

        self.dt = 0
        self.current_fps = 0

    def run(self):
        info("Starting update cycle..")
        while not self.done:
            self.dt = self.clock.tick(clock.target_fps) / 1000
            camera.main.update()
            self.run_logic()
            self.draw()
            self.handle_events()
            manager.manager.update(self.dt)
            self.current_fps = self.clock.get_fps()
            events.keyboard_list.clear()
        info("Goodbye!")
        pg.quit()


    def handle_events(self):
        Events()
        [m() for m in update_methods]
        for event in events.event_list:
            manager.manager.process_events(event)
            if event.type == pg.QUIT:
                self.done = True

    def run_logic(self):
        if self.current_fps > 0:
            space.iterations = Settings.iterations
            steps = Settings.steps
            for _ in range(0,steps):
                space.step((1*self.dt/steps))

        [m() for m in logic_methods]

    def draw(self):
        self.screen.fill(pg.Color(134, 183, 181))
        [m() for m in draw_methods]
        manager.manager.draw_ui(self.screen)
        pg.display.flip()

