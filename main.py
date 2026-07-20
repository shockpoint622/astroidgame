import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #main game loop
    while True:
        #log the current state of the game in jsonl file
        log_state()
        #logic for closing/quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #blank starting screen for initial testing perposes
        screen.fill("black")
        user: Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        user.draw(screen)
        #refreshes the screen at the end of the loop
        dt = clock.tick(60) / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()
