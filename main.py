# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((1280, 720))

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

if __name__ == "__main__":
    main()

