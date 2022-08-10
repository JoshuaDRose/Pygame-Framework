"""game.particle
game module for simulating particles.
The particle module can use basic physics to simulate movement.
Sin radius which uses a pygame.SRCALPHA is in the process of being implemented.
"""


import math
import pygame
import random
from .entity import Entity


class Spark():
    """ https://dafluffypotato.com/static/scripts/sparks_vfx.py """
    def __init__(self, location, angle, velocity, color, scale=1):
        self.location = location
        self.angle = angle
        self.scale = scale
        self.pos_type = ''
        self.velocity = velocity
        self.color = color
        self.alive = True
        self.r = False
        self.g = False
        self.b = False
        self.color_velocity = 10
        if self.pos_type == 'random':
            mx = random.randint(location[0]-25, location[0]+25)
            my = random.randint(location[1]-25,location[1]+25)

            self.location = [mx,my]
            print((mx,my,self.location))


    def point_towards(self, angle, rate):
        rotation_direction = ((angle - self.angle + math.pi * 3) % (math.pi * 2)) - math.pi
        try:
            rotate_sign = abs(rotation_direction) / rotation_direction
        except ZeroDivisionError:
            rotate_sign = 1
        if abs(rotation_direction) < rate:
            self.angle = angle
        else:
            self.angle += rate * rotate_sign

    def calculate_movement(self, dt):
        return [math.cos(self.angle) * self.velocity * dt, math.sin(self.angle) * self.velocity * dt]

    def adjust_velocity(self, friction, force, terminal_velocity, dt):
        movement = self.calculate_movement(dt)
        movement[1] = min(terminal_velocity, movement[1] + force * dt)
        movement[1] *= friction
        self.angle = math.atan2(movement[1], movement[0])

    def update(self, dt):
        movement = self.calculate_movement(dt)
        self.location[0] += movement[0]
        self.location[1] += movement[1]
        # self.velocity -= random.choice([0.05,0.1,0.15])
        self.velocity -= .1
        if self.color != [255,255,255]:
            if self.r and self.g and self.b:
                if self.color[0] > 90:
                    self.color[0] -= 1
                if self.color[1] < 180:
                    self.color[1] += self.color_velocity
                if self.color[2] < 200:
                    self.color[2] += self.color_velocity
            else:
                if self.color[0] > 245:
                    self.color[0] -= self.color_velocity
                if self.color[1] > 50:
                    self.color[1] -= self.color_velocity
                if self.color[2] < 40:
                    self.color[2] += self.color_velocity
                if self.color[0] == 240:
                    self.r = True
                if self.color[1] == 50:
                    self.g = True
                if self.color[2] == 40:
                    self.b = True
        else:
            pass

        if self.velocity <= 0:
            self.alive = False

    def draw(self, surface, offset=[0, 0]):
        if self.alive:
            points = [
                    [self.location[0] + math.cos(self.angle) * self.velocity * self.scale, self.location[1] + math.sin(self.angle) * self.velocity  * self.scale],
                    [self.location[0] + math.cos(self.angle + math.pi / 2) * self.velocity * self.scale * 0.3, self.location[1] + math.sin(self.angle + math.pi / 2) * self.velocity * self.scale * 0.3],
                    [self.location[0] - math.cos(self.angle) * self.velocity * self.scale * 3.5, self.location[1] - math.sin(self.angle) * self.velocity* self.scale * 3.5],
                    [self.location[0] + math.cos(self.angle - math.pi / 2) * self.velocity * self.scale * 0.3, self.location[1] - math.sin(self.angle + math.pi / 2) * self.velocity * self.scale * 0.3]
                    ]
            pygame.draw.polygon(surface, self.color, points)

class Particle():
    """ Particle system used for game """
    def __init__(self, radius, velocity, alpha_value):
        """ Constructor takes in extensive arguments """
        self.radius = radius
        self.velocity = velocity
        self.alpha_value = alpha_value

    def update, dt(self):
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
        self.radius = math.sin(dt * 5) * 5 + self.radius
        pygame.draw.circle(self.image, self.color, self.radius, self.position, 0)


