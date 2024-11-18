#main
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    pygame.display.set_caption("Asteroids Game")
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Close the window
                running = False

        screen.fill((0, 0, 0))  # Clear the screen
        player.draw(screen)     # Draw the player
        pygame.display.flip()   # Update the display
        clock.tick(60)

    pygame.quit()  # Clean up and close the game


if __name__ == "__main__":
    main()
