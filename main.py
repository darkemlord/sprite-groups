import pygame as pg
from Characters.monster import Monster
from Characters.player import Knight

# Initialize Pygame
pg.init()

# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Sprite groups")

# set fps and clock
FPS = 60
clock = pg.time.Clock()

# Create a sprite group for the monsters
monster_group = pg.sprite.Group()
for i in range(10):
    monster = Monster(i * 64, 10)
    monster_group.add(monster)

# Create the Knight
knight_group = pg.sprite.Group()
knight = Knight(500, 500, monster_group)
knight_group.add(knight)

# the main game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # Fill the display
    display_surface.fill((0, 0, 0))

    # Update and draw assets
    knight_group.update()
    knight_group.draw(display_surface)
    monster_group.update()
    monster_group.draw(display_surface)

    # Update the display and tick the clock
    pg.display.update()
    clock.tick(FPS)
# End of the game loop
pg.quit()
