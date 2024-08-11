import pygame as pg
import random


class Monster(pg.sprite.Sprite):
    """A simple class to represent a spooky monster"""

    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load("./assets/blue_monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 10)

    def update(self):
        """Move the monster"""
        self.rect.y += self.velocity
