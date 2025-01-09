import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SCALE_SPEED

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position.x = x
        self.position.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 7)

    def update(self, dt):
        self.position += self.velocity * dt # Update the position using velocity and delta

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS: # Small asteroid hit, don't spawn new asteroids
            return
        else:
            asteroid_split_angle = self.__generate_random_angle()
            split_vector_1, split_vector_2 = (self.__build_split_vectors
                                              (asteroid_split_angle))
            self.__spawn_new_asteroids(split_vector_1, split_vector_2)

    def __generate_random_angle(self):
        return random.uniform(20.0, 50.0)
    
    def __build_split_vectors(self, angle):
        new_vector_1 = pygame.math.Vector2.rotate(self.velocity, angle)
        new_vector_2 = pygame.math.Vector2.rotate(self.velocity, -angle)
        return new_vector_1, new_vector_2
    
    def __spawn_new_asteroids(self, vector1, vector2):
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = vector1 * ASTEROID_SPLIT_SCALE_SPEED
        asteroid_2.velocity = vector2 * ASTEROID_SPLIT_SCALE_SPEED