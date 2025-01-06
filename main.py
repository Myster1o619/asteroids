# this allows us to use code from
# the open-source pygame library
# throughout this file

# activate virutal environ:
# source venv/bin/activate

import pygame
from constants import *
from player import Player
from asteroid import Asteroid

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    # Add a clock to limit the frame rate.
    clock = pygame.time.Clock()

    dt = None

    player_object = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_object = Asteroid(60, 60, 20)
    asteroid_object.velocity = 200

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    updatable.add(player_object, asteroid_object)
    drawable.add(player_object, asteroid_object)
    asteroids.add(asteroid_object)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         return

        
        dt = clock.tick(60) / 1000
        screen.fill((0,0,0))

        for item in drawable:
            item.draw(screen)
        
        for item in updatable:
            item.update(dt)

        pygame.display.flip() # Update the display shown on the screen
        clock.tick(60) # Limit the frame rate to 60 FPS.
        

if __name__ == "__main__":
    main()

