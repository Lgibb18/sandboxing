import Scripts.Engine.sprites
from Scripts.Engine.utils import *
from Scripts.Engine.entity import *
from Scripts.Components.PhysicsComponent import *
from Scripts.Components.SpriteComponent import *
from Scripts.Components.DraggableComponent import *
from Scripts.Engine.sprites import *
from Scripts.Engine.component import *
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
        self.static_lines = [
            pm.Segment(self.space.static_body, flipy((0, 780.0)), flipy((1280.0, 780.0)), 20),
            ]
        for lin in self.static_lines:
            lin.friction = 0.2
            lin.elasticity = 0.99
            self.space.add(lin)
        self.all_entities : list[Entity] = []
        self.dragging_object = None
        self.mrel = (0,0)

    def run(self):
        while not self.done:
            if self.dragging_object != None:
                self.dragging_object.transform.position = pg.mouse.get_pos()
                print(get_component(PhysicsComponent, self.dragging_object)[0])
                if (get_component(PhysicsComponent, self.dragging_object)[0]):
                    print(pg.mouse.get_rel())
                    b: PhysicsComponent = get_component(PhysicsComponent, self.dragging_object)[1]
                    b.body.position = flipy(pg.mouse.get_pos())
                    b.shape.body.velocity = Vec2d(self.mrel[0] *5, -self.mrel[1] *5)
                    print(str(b.shape.body.velocity.x) + ", " + str(b.shape.body.velocity.y))
            self.dt = self.clock.tick(60) / 1000
            self.run_logic()
            self.draw()
            self.handle_events()
            self.current_fps = self.clock.get_fps()
            self.mrel = pg.mouse.get_rel()

        pg.quit()


    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_e:  # Left mouse button.
                    # Spawn an entity.
                    def_entity = Entity(
                        "PhysicsObject",
                        Transform(pg.mouse.get_pos(), (50, 50)),
                        [
                            SpriteComponent(pg.image.load("Sprites/db.png"), LAYER_4_OBJECTS),
                            PhysicsComponent(self.space),
                        ]
                    )
                    self.all_entities.append(def_entity)
                if event.key == pg.K_q:  # Left mouse button.
                    # Spawn an entity.
                    def_entity = Entity(
                        "NahObject",
                        Transform(pg.mouse.get_pos(), (50, 50)),
                        [
                            SpriteComponent(pg.image.load("Sprites/random.png"), LAYER_5_OVER_OBJECTS)
                        ]
                    )
                    self.all_entities.append(def_entity)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for entity in self.all_entities:
                        if(collision_check(pg.mouse.get_pos(), entity.transform.position, entity.transform.scale)):
                            self.dragging_object = entity
                            break
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dragging_object = None




    def run_logic(self):
        self.space.step(1/60)
        self.sprites.run_logic()
        for obj in self.all_entities:
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