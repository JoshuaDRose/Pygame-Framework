"""game.particle
game module for simulating particles.

The particle module can use basic physics to simulate movement.

Sin radius which uses a pygame.SRCALPHA is in the process of being implemented 
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
        # (255, 119, 0) - fire orange
        # (247, 52, 43) - lava red
        # (94,186,201) - fire blue
        # ORDER = ORANGE -> RED -> BLUE
        # ---- COLOR PROGRESSION --- #
        """
            [255, 255, 255]
            [254.75, 254.75, 254.75]
            [254.5, 254.5, 254.5]
            [254.25, 254.25, 254.25]
            [254.0, 254.0, 254.0]
            [253.75, 253.75, 253.75]
            [253.5, 253.5, 253.5]
            [253.25, 253.25, 253.25]
            [253.0, 253.0, 253.0]
            [252.75, 252.75, 252.75]
            [252.5, 252.5, 252.5]
            [252.25, 252.25, 252.25]
            [252.0, 252.0, 252.0]
            [251.75, 251.75, 251.75]
            [251.5, 251.5, 251.5]
            [251.25, 251.25, 251.25]
            [251.0, 251.0, 251.0]
            [250.75, 250.75, 250.75]
            [250.5, 250.5, 250.5]
            [250.25, 250.25, 250.25]
            [250.0, 250.0, 250.0]
            [249.75, 249.75, 249.75]
            [249.5, 249.5, 249.5]
            [249.25, 249.25, 249.25]
            [249.0, 249.0, 249.0]
            [248.75, 248.75, 248.75]
            [248.5, 248.5, 248.5]
            [248.25, 248.25, 248.25]
            [248.0, 248.0, 248.0]
            [247.75, 247.75, 247.75]
            [247.5, 247.5, 247.5]
            [247.25, 247.25, 247.25]
            [247.0, 247.0, 247.0]
            [247.0, 246.75, 246.75]
            [247.0, 246.5, 246.5]
            [247.0, 246.25, 246.25]
            [247.0, 246.0, 246.0]
            [247.0, 245.75, 245.75]
            [247.0, 245.5, 245.5]
            [247.0, 245.25, 245.25]
            [247.0, 245.0, 245.0]
            [247.0, 244.75, 244.75]
            [247.0, 244.5, 244.5]
            [247.0, 244.25, 244.25]
            [247.0, 244.0, 244.0]
            [247.0, 243.75, 243.75]
            [247.0, 243.5, 243.5]
            [247.0, 243.25, 243.25]
            [247.0, 243.0, 243.0]
            [247.0, 242.75, 242.75]
            [247.0, 242.5, 242.5]
            [247.0, 242.25, 242.25]
            [247.0, 242.0, 242.0]
            [247.0, 241.75, 241.75]
            [247.0, 241.5, 241.5]
            [247.0, 241.25, 241.25]
            [247.0, 241.0, 241.0]
            [247.0, 240.75, 240.75]
            [247.0, 240.5, 240.5]
            [247.0, 240.25, 240.25]
            [247.0, 240.0, 240.0]
            [247.0, 239.75, 239.75]
            [247.0, 239.5, 239.5]
        """
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

