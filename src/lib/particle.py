"""game.particle
game module for simulating particles.

The particle module can use basic physics to simulate movement.

Sin radius which uses a pygame.SRCALPHA is in the process of being implemented 
"""


import math
import pygame 
from .entity import Entity


class Particle(Entity):
    """ Particle system used for game """
    def __init__(self, rect, radius, velocity, alpha_value):
        """ Constructor takes in extensive arguments """
        self.rect = rect
        self.radius = radius
        self.velocity = velocity
        self.alpha_value = alpha_value
        Entity.__init__([radius, radius], [rect[0], rect[1]])

    def update(self):
        """ Updates all sprites in particle group """
        self.color.append(self.alpha_value)
        self.radius -= .3
        if self.color == [0, 0, 0]:
            for index in enumerate(self.color):
                self.color[index] += 1

        elif self.color == [255, 255, 255]:
            for index in enumerate(self.color):
                self.color[index] -= 1
        
        self.position[0] += self.velocity[0]
        self.position[1] += math.cos(self.velocity[0])
        # wave = (object_magnitude + (time * velocity) * magnitude + position)
        self.radius = math.sin(pygame.time.get_ticks() * 5) * 5 + self.radius
        pygame.draw.circle(self.image, self.color, self.radius, self.position, 0)

    def remove_particles(self, particles):
        """ Remove all particles from sprite group """
        for particle in particles:
            particles.remove(particle)

