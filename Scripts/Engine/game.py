from Scripts.Engine.utils import *
from Scripts.Engine.entity import *
from Scripts.Components.PhysicsComponent import *
from Scripts.Components.SpriteComponent import *
from Scripts.Engine.sprites import *
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1280, 800))
        self.done = False
        self.clock = pg.time.Clock()
        icon = pg.image.load("Sprites/db.png")
        pg.display.set_icon(icon)
        pg.display.set_caption('Nighty box 2', 'nb2')
        # Pymunk stuff
        self.space = pm.Space()
        self.space.gravity = Vec2d(0.0, -900.0)
        self.space.damping = .9
        self.static_lines = [
            pm.Segment(self.space.static_body, flipy((0, 780.0)), flipy((1280.0, 780.0)), 20),
            ]
        for lin in self.static_lines:
            lin.friction = 0.2
            lin.elasticity = 0.99
            self.space.add(lin)
        self.all_objects = []
        self.sprites = Sprites(self.screen)

    def run(self):
        while not self.done:
            self.dt = self.clock.tick(60) / 1000
            self.run_logic()
            self.draw()
            self.handle_events()
            self.current_fps = self.clock.get_fps()

        pg.quit()


    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button.
                    # Spawn an entity.
                    def_entity = Entity(
                        "PhysicsObject",
                        Transform(pg.mouse.get_pos(), (50, 50)),
                        [SpriteComponent(pg.image.load("Sprites/db.png"), self.sprites), PhysicsComponent(self.space)]
                    )
                    self.all_objects.append(def_entity)
                if event.button == 3:  # Left mouse button.
                    # Spawn an entity.
                    def_entity = Entity(
                        "DefaultObject",
                        Transform(pg.mouse.get_pos(), (50, 50))
                    )
                    self.all_objects.append(def_entity)


    def run_logic(self):
        self.space.step(1/60)
        self.sprites.run_logic()
        for obj in self.all_objects:
            obj.update()

    def draw(self):
        self.screen.fill(pg.Color(134, 183, 181))
        self.sprites.draw()
        for line in self.static_lines:
            body = line.body
            p1 = flipy(body.position + line.a.rotated(body.angle))
            p2 = flipy(body.position + line.b.rotated(body.angle))
            pg.draw.lines(self.screen, pg.Color('lightgray'), False, (p1, p2), 40)
        pg.display.flip()