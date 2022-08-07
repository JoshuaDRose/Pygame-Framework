import pygame
from .entity import Entity

class Enemy(Entity):
    """ Inherit entity class as Enemy uses pygame.sprite.Sprite """
    def __init__(self, size, position):
        """ enemy constructor """
        self.size = size
        self.position = position
        self.border = pygame.Surface(size)
        Entity.__init__(self, size, position)

    def update(self):
        """ Override update function in sprite.update """
        self.border.blit(self.image)

    def draw(self):
        """ draw to surface """
        self.border.blit(self.image)


