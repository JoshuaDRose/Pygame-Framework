"""
Author: Joshua Rose 2022
joshuarose099@gmail.com
The __main__.py files ensures backwards directory execution compatability
"""


import os
import sys

import pygame
from pygame.locals import QUIT

from dataclasses import dataclass

import lib


__all__ = []


class Game(lib.Window):
    """ source game loop from __main__ """
    def __init__(self, size, flags): 
        """ Game sequence constructor """
        lib.Window.__init__(self, size, flags)
        self.done = False
        self.particles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.player.add(lib.Player([50, 50]))
        self.clock = pygame.time.Clock()
        self.sprites = {
            'characters': os.path.join('data/sprites', 'characters.png'),
            'swoosh': os.path.join('data/sprites', 'swoosh.png'),
            'tiles': os.path.join('data/tiles', 'tiles.png')
        }

    def run(self):
        """ primary game sequence method """
        while not self.done:
            mouse_position = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_escape:
                        self.done = True
            pygame.display.update()
            self.clock.tick(60)
        self.exit_window()


game = Game([960, 540], pygame.SHOWN)

if __name__ == "__main__":
    game.run()
