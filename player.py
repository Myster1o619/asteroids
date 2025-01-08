import pygame
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0.00
        self.first_shot_fired = False

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            if not self.first_shot_fired:
                self.shoot_timer = self.set_player_shoot_timer()
                self.first_shot_fired = True
                self.__create_and_update_bullet(dt)
            elif self.first_shot_fired and self.shoot_timer <= 0:
                self.shoot_timer = self.set_player_shoot_timer()
                self.__create_and_update_bullet(dt)
            else:
                pass
            self.shoot_timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        forward = pygame.Vector2(0, 1)
        direction = forward.rotate(self.rotation)
        velocity = direction * PLAYER_SHOOT_SPEED
        new_shot.velocity = velocity
        return new_shot
    
    def __create_and_update_bullet(self, dt):
        new_bullet = self.shoot()
        new_bullet.update(dt)

    def set_player_shoot_timer(self):
        return PLAYER_SHOOT_COOLDOWN
        