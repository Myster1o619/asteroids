# this allows us to use code from
# the open-source pygame library
# throughout this file

# activate virutal environ:
# source venv/bin/activate

import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    # Add a clock to limit the frame rate.
    clock = pygame.time.Clock()

    dt = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         return


        screen.fill((0,0,0))
        # pygame.display.update()
        pygame.display.flip()
        clock.tick(60) # Limit the frame rate to 60 FPS.
        dt = 1000 / clock.tick(60)

if __name__ == "__main__":
    main()

