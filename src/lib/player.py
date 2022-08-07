import pygame
from .entity import Entity

class Player(Entity):
    """ Inherit entity class as player is a sprite """
    def __init__(self, size):
        """ Player class constructor """
        self.size = size
        self.position = [100, 100]
        Entity.__init__(self, self.size, self.position)
        self.jump_count = 10
        self.jump_velocity: int = ...

    def jump(self):
        """ Jump method """
        for i in enumerate(self.jump_count):
            if i > 0:
                self.movement[1] += self.jump_velocity

