import math
import pygame


class Planet:

    # Properties
    color = None
    size = 0
    orbit_speed = 0
    pos_x = 0
    pos_y = 0
    origin = None
    orbit_radius = 0
    _angle = 0

    def __init__(self, color=(255, 255, 255), size=1, orbit_speed=1, origin=(0, 0), orbit_radius=100):
        self.color = color
        self.size = size
        self.orbit_speed = orbit_speed
        self.origin = origin
        self.orbit_radius = orbit_radius

    def update(self):
        self._angle += (0.10472 * self.orbit_speed)

        self.pos_x = int(self.origin[0] + math.cos(self._angle) * self.orbit_radius)
        self.pos_y = int(self.origin[1] + math.sin(self._angle) * self.orbit_radius)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos_x), int(self.pos_y)), self.size)
