import pygame as pg


class Sprites:
    def __init__(self, screen):
        self.all_sprites = pg.sprite.Group()
        self.screen = screen

    def run_logic(self):
        self.all_sprites.update()

    def draw(self):
        self.all_sprites.draw(self.screen)  # Draw the images of all sprites.