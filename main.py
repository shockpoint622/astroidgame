import pygame

from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    user: Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field: AsteroidField = AsteroidField()

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

        updatable.update(dt)

        for d in drawable:
            d.draw(screen)
        #refreshes the screen at the end of the loop
        dt = clock.tick(60) / 1000

        pygame.display.flip()


if __name__ == "__main__":
    main()
