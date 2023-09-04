import pygame
from player import *
from renderer import *

pygame.init()

class App():
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.win_size = (1000, 1000)
        self.win = pygame.display.set_mode(self.win_size, pygame.RESIZABLE)

        self.theta = 0

    def draw(self):
        self.win.fill((5, 0, 35))
        #render_cube(self.win, 100, self.player.theta, self.player.x, self.player.y - 1)
        #render_cube(self.win, 100, self.player.theta, self.player.x - 1, self.player.y - 0)
        render_cube(self.win, 100, self.player.theta, self.player.x - 0, self.player.y - 0)
        render_cube(self.win, 100, self.player.theta, self.player.x - 1, self.player.y - 0)
        render_cube(self.win, 100, self.player.theta, self.player.x + 1, self.player.y - 0)
        #render_cube(self.win, 100, self.player.theta, self.player.x + 1, self.player.y - 0)
        #render_cube(self.win, 100, self.player.theta, self.player.x, self.player.y + 1)
        pygame.display.flip()

    def update(self):
        print(self.player.x, self.player.y)
        self.draw()

    def start_app(self):

        self.player = Player()

        self.run = True
        while self.run:
            self.dt = self.clock.tick()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
            
            keys = pygame.key.get_pressed()
            self.player.input(keys, self.dt)
            
            self.update()

game = App()
game.start_app()