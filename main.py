import pygame

from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
import random

random.seed(1)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

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
        for ast in asteroids:
            if ast.collides_with(user):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if ast.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    ast.split()



        for d in drawable:
            d.draw(screen)
        #refreshes the screen at the end of the loop
        dt = clock.tick(60) / 1000

        pygame.display.flip()


if __name__ == "__main__":
    main()
