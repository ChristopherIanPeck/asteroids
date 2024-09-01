import pygame
from pygame.locals import *
from constants import *


class Player(x, y):
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        dt = clock.tick(60)/1000
        player.draw(screen)


if __name__ == "__main__":
    main()
