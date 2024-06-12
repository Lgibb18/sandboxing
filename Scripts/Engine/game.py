import Scripts.Engine.sprites
from Scripts.Engine.utils import *
from Scripts.Engine.entity import *
from Scripts.Components.PhysicsComponent import *
from Scripts.Components.SpriteComponent import *
from Scripts.Components.DraggableComponent import *
from Scripts.Engine.sprites import *
from Scripts.Engine.component import *
from Scripts.Engine.events import *
all_entities : list[Entity] = []
import Scripts.Engine.sprites as sprites
import Scripts.Engine.camera as camera

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1280, 800))
        self.sprites = Sprites(self.screen)
        Scripts.Engine.sprites.every_sprites = self.sprites
        self.done = False
        self.clock = pg.time.Clock()
        icon = pg.image.load("Sprites/db.png")
        pg.display.set_icon(icon)
        pg.display.set_caption('Nighty box 2', 'nb2')
        # Pymunk stuff
        self.space = pm.Space()
        self.space.gravity = Vec2d(0.0, -900.0)
        self.space.damping = .9

        def_entity = Entity(
            "Ground",
            Transform((1280/2,800), (1280, 50)),
            [
                SpriteComponent(pg.image.load("Sprites/white.png"), LAYER_1_GROUND),
                PhysicsComponent(self.space, pm.Body.STATIC)
            ]
        )
        all_entities.append(def_entity)
    def run(self):
        while not self.done:
            self.dt = self.clock.tick(60) / 1000
            camera.main.update()
            self.run_logic()
            self.draw()
            self.handle_events()
            self.current_fps = self.clock.get_fps()

        pg.quit()


    def handle_events(self):
        Events()
        for event in Scripts.Engine.events.event_list:
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_e:  # Left mouse button.
                    # Spawn an entity.
                    def_entity = Entity(
                        "PhysicsObject",
                        Transform(camera.mouse_pos(), (50, 50)),
                        [
                            SpriteComponent(pg.image.load("Sprites/db.png"), LAYER_4_OBJECTS),
                            PhysicsComponent(self.space),
                            DraggableComponent()
                        ]
                    )
                    all_entities.append(def_entity)
                if event.key == pg.K_q:  # Left mouse button.
                    # Spawn an entity.
                    def_entity = Entity(
                        "NahObject",
                        Transform(camera.mouse_pos(), (50, 50)),
                        [
                            SpriteComponent(pg.image.load("Sprites/random.png"), LAYER_5_OVER_OBJECTS),
                            DraggableComponent()
                        ]
                    )
                    all_entities.append(def_entity)






    def run_logic(self):
        self.space.step(1/60)
        self.sprites.run_logic()
        for obj in all_entities:
            obj.update()


    def draw(self):
        self.screen.fill(pg.Color(134, 183, 181))
        self.sprites.draw()
        pg.display.flip()
