"""
Author: Joshua Rose 2022
joshuarose099@gmail.com
The __main__.py files ensures backwards directory execution compatability
"""

import os
import sys
import math
import random

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
        self.particles = []
        self.sparks = []
        self.player = pygame.sprite.GroupSingle()
        self.player.add(lib.Player([50, 50]))
        self.clock = pygame.time.Clock()
        self.sprites = {
            'characters': os.path.join('data/sprites', 'characters.png'),
            'swoosh': os.path.join('data/sprites', 'swoosh.png'),
            'tiles': os.path.join('data/tiles', 'tiles.png')
        }
        self.collision_sparks = []
        self.draw_sparks = False
        self.spark_cap = 5
        self.previous_cap = 1
        self.do_gradient = False
        self.particle_keys = False #  declare if particle can be activated by keys

    def run(self):
        """ primary game sequence method """
        while not self.done:
            self.display.fill((0,0,0))
            for index, spark in sorted(enumerate(self.sparks), reverse=True):
                spark.update(1)
                spark.draw(self.display)
                if not spark.alive:
                    self.sparks.pop(index)

            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
                    elif event.key == pygame.K_c:
                        if self.particle_keys:
                            print(f"[particle system] Setting do_gradient to {not self.do_gradient}")
                            self.do_gradient = not self.do_gradient
                    elif event.key == pygame.K_UP:
                        if self.particle_keys:
                            self.spark_cap += 1
                            print(f"[particle system] Increasing entity limit to {self.spark_cap}")
                    elif event.key == pygame.K_DOWN:
                        if self.particle_keys:
                            if self.spark_cap > 1:
                                print(f"[particle system] Decreasing entity limit to {self.spark_cap}")
                                self.spark_cap -= 1
                    elif event.key == pygame.K_SPACE:
                        if self.particle_keys:
                            self.draw_sparks = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if self.particle_keys:
                            self.draw_sparks = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.particle_keys:
                        self.previous_cap = self.spark_cap
                        self.spark_cap = 0
                        self.draw_sparks = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.particle_keys:
                        self.spark_cap =self.previous_cap
                        self.draw_sparks = False


            if self.draw_sparks:
                if self.spark_cap == 0:
                    if self.do_gradient:
                        self.sparks.append(lib.Spark([mx,my], math.radians(random.randint(0,360)), random.randint(3, 6), [250, 110, 0], random.randint(1,2)))
                    else:
                        self.sparks.append(lib.Spark([mx,my], math.radians(random.randint(0,360)), random.randint(3, 6), [255,255,255], random.randint(1,2)))
                if len(self.sparks) < self.spark_cap:
                    if self.do_gradient:
                        self.sparks.append(lib.Spark([mx,my], math.radians(random.randint(0,360)), random.randint(3, 6), [250, 110, 0], random.randint(1,2)))
                    else:
                        self.sparks.append(lib.Spark([mx,my], math.radians(random.randint(0,360)), random.randint(3, 6), [255,255,255], random.randint(1,2)))

            pygame.display.update()
            self.clock.tick(60)
        self.exit_window()


game = Game([960, 540], pygame.SHOWN)

if __name__ == "__main__":
    game.run()
