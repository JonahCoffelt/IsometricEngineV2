import pygame
from math import *

class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.theta = 0
        
        self.move_speed = .005
        self.turn_speed = .005
    
    def move(self, dt, dx, dy):
        self.y += sin(self.theta + pi/4) * dy * self.move_speed * dt
        self.x += cos(self.theta + pi/4) * dx * self.move_speed * dt
    
    def input(self, inputs, dt):
        if inputs[pygame.K_w]:
            if inputs[pygame.K_a]: self.move(dt, -sqrt(2) / 2, sqrt(2) / 2)
            elif inputs[pygame.K_d]: self.move(dt, sqrt(2) / 2, sqrt(2) / 2)
            elif not inputs[pygame.K_s]: self.move(dt, 0, 1)
        elif inputs[pygame.K_s]:
            if inputs[pygame.K_a]: self.move(dt, -sqrt(2) / 2, -sqrt(2) / 2)
            elif inputs[pygame.K_d]: self.move(dt, sqrt(2) / 2, -sqrt(2) / 2)
            else: self.move(dt, 0, -1)
        elif inputs[pygame.K_d]:
            if not inputs[pygame.K_a]: self.move(dt, 1, 0)
        elif inputs[pygame.K_a]:
            self.move(dt, -1, 0)
        
        if inputs[pygame.K_RIGHT]:
            self.theta += .002 * dt
        if inputs[pygame.K_LEFT]:
            self.theta -= .002 * dt
