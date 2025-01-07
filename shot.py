import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position.x = x
        self.position.y = y
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 1)

    def update(self, dt):
        self.position += self.velocity * dt # Update the position using velocity and delta