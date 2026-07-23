from circleshape import CircleShape
import pygame
from constants import *
from logger import *
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x,y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt) -> None:
        assert isinstance(self.velocity, pygame.Vector2), f"{self} has bad velocity: {self.velocity!r}"
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        angle_new1 = self.velocity.rotate(angle)
        angle_new2 = self.velocity.rotate(angle * -1)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        aster1 = Asteroid(self.position.x, self.position.y, new_rad)
        aster1.velocity = angle_new1 * 1.2
        aster2 = Asteroid(self.position.x, self.position.y, new_rad)
        aster2.velocity = angle_new2 * 1.2
