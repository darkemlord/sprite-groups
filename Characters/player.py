import pygame as pg


class Knight(pg.sprite.Sprite):
    """A class to represent the knight who fights the monsters"""

    def __init__(self, x, y, monster_group):
        super().__init__()
        self.image = pg.image.load("./assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.monster_group = monster_group

        self.velocity = 5

    def update(self):
        """Move the knight"""
        self.move()
        self.check_collisions()

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pg.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pg.K_UP]:
            self.rect.y -= self.velocity
        if keys[pg.K_DOWN]:
            self.rect.y += self.velocity

    def check_collisions(self):
        """Check if the knight is colliding with the screen edges and monsters"""
        pg.sprite.spritecollide(self, self.monster_group, True)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600


# End of the Knight class
