# this allows us to use code from
# the open-source pygame library
# throughout this file

# activate virutal environ:
# source venv/bin/activate

import pygame
from constants import *
from player import Player

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

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         return


        screen.fill((0,0,0))
        player_object.draw(screen) # Render the player object to the screen
        player_object.update(dt)
        pygame.display.update()
        pygame.display.flip() # Update the display shown on the screen
        clock.tick(60) # Limit the frame rate to 60 FPS.
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

