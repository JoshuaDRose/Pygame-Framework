import pygame
from .entity import Entity

class Player(Entity):
    """ Inherit entity class as player is a sprite """
    def __init__(self, position):
        """ Player class constructor. Note the player is loaded from an image file """
        self.position = [100, 100]
        # self.player = pygame.image.load('data/sprites/characters.png').convert_alpha()
        self.player = pygame.Surface([50,50])
        self.rect = self.player.get_rect()
        self.size = [self.rect.width, self.rect.height]
        Entity.__init__(self, self.size, self.position)
        self.jump_count = 10
        self.jump_velocity: int = ...

    def jump(self):
        """ Jump method """
        for i in enumerate(self.jump_count):
            if i > 0:
                self.movement[1] += self.jump_velocity

