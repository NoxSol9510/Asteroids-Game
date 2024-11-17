import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    pygame.display.set_caption("Asteroids Game")
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Close the window
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()  # Clean up and close the game


if __name__ == "__main__":
    main()