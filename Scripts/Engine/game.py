import Scripts.Engine.sprites
from Scripts.Engine.utils import *
from Scripts.Engine.entity import *
from Scripts.Components.PhysicsComponent import *
from Scripts.Components.SpriteComponent import *
from Scripts.Components.DraggableComponent import *
from Scripts.Engine.sprites import *
from Scripts.Engine.component import *
from Scripts.Engine.events import *
import Scripts.Engine.sprites as sprites
import Scripts.Engine.camera as camera
from Scripts.Engine.console import *
import Scripts.Engine.events as events
from Scripts.Engine.inventory import *
from Scripts.Engine.entities import *
space = pm.Space()
class Game:
    def __init__(self):
        pg.init()
        self.resolution = (1280, 720)
        self.screen = pg.display.set_mode(self.resolution, pg.RESIZABLE)
        self.sprites = Sprites(self.screen)
        Scripts.Engine.sprites.every_sprites = self.sprites
        self.console = Console(self.screen)
        self.inventory = Inventory(self.screen)
        self.done = False
        self.clock = pg.time.Clock()
        icon = pg.image.load("Sprites/db.png")
        pg.display.set_icon(icon)
        pg.display.set_caption('Nighty box 2', 'nb2')
        # Pymunk stuff
        #self.space = pm.Space()
        space.gravity = Vec2d(0.0, -900.0)
        space.damping = .9
        Instantiate("map", Transform((self.resolution[0] / 2,self.resolution[1]), (self.resolution[0]*50, 50)))
    def run(self):
        while not self.done:
            self.dt = self.clock.tick(60) / 1000
            camera.main.update()
            self.run_logic()
            self.draw()
            self.handle_events()
            self.current_fps = self.clock.get_fps()
            events.keyboard_list.clear()

        pg.quit()


    def handle_events(self):
        Events()
        self.inventory.update()
        self.console.update()
        for event in events.event_list:
            if event.type == pg.QUIT:
                self.done = True






    def run_logic(self):
        space.step(1/60)
        entities_update()
        self.sprites.run_logic()


    def draw(self):
        self.screen.fill(pg.Color(134, 183, 181))
        self.sprites.draw()
        self.inventory.draw()
        self.console.draw()
        pg.display.flip()
