import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Immediately kill the current asteroid
        self.kill()

        # If the asteroid is at the minimum size, do not split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Small asteroid disappears when destroyed

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current velocity
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Increase speed by 20%
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Calculate the new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new Asteroid objects at the current position with the new radius
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Set their velocities
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2
