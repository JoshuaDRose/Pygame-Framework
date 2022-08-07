import pygame 

class Entity(pygame.sprite.Sprite):
    """ Used as a base class for pygame.sprite.Sprite (s) """
    def __init__(self, size, position):
        self.size = size
        self.position = position
        pygame.sprite.Sprite.__init__(self)
        self.movement = []

    def update(self):
        """ Update entity position """
        self.position[0] += self.movement[0]
        self.position[1] += self.movement[1]

    def draw(self):
        """ Draw to surface """
        self.image.rect = self.image.get_rect()

