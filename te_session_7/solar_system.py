# Draw a model of a solar system in scale (planet size, orbit speed and distance from sun (optional))

import pygame
from te_session_7.Planet import Planet

pygame.init()
clock = pygame.time.Clock()
# CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

# Planets
earth = Planet((15, 25, 198), 10, 1, (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)), 100)
mars = Planet((198, 72, 15), 4, 0.7, (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)), 140)

while not done:
    # Reset the screen
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Draw stuff
    pygame.draw.circle(screen, (252, 240, 10), (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)), 50)

    earth.update()
    mars.update()

    earth.draw(screen)
    mars.draw(screen)

    pygame.display.flip()

    clock.tick(60)
