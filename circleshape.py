import pygame
import math

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y) # Starting position of the circle
        self.velocity = pygame.Vector2(0, 0) # Speed and direction
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def distance_to(self, circle_object):
        return math.sqrt(
            (circle_object.position.x - self.position.x) ** 2 +
            (circle_object.position.y - self.position.y) ** 2 -
            (circle_object.radius + self.radius)
            )
    
    def detect_collision(self, circle_object):
        distance = self.distance_to(circle_object)
        if distance <= circle_object.radius + self.radius:
            return True
        return False