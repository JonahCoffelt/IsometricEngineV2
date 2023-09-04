import pygame
from numpy import *

def render_cube(win, scale, theta, dx, dy):
    theta = theta % (pi * 2)
    r = sqrt(dx ** 2 + dy ** 2)

    #dy2 = (dx*sin(-theta + (7 * pi / 4)) - dy*cos(-theta + (7 * pi / 4))) * scale * .7
    #dx2 = (dx*sin(-theta + (pi / 4)) - dy*cos(-theta + (pi / 4))) * scale * 1.2248
    #dy = dy2
    #dx = dx2

    dx = r * cos(theta) * scale
    dy = r * sin(theta) * scale

    a1 = (500 + scale * (cos(theta + (3 * pi / 2)) * (sqrt(3) / 2)) + dx, 500 + -scale * (sin(theta + (3 * pi / 2)) / 2 + .5) + dy)
    b1 = (500 + scale * (cos(theta + (pi)) * (sqrt(3) / 2)) + dx, 500 + -scale * (sin(theta + (pi)) / 2 + .5) + dy)
    c1 = (500 + scale * (cos(theta + (pi / 2)) * (sqrt(3) / 2)) + dx, 500 + -scale * (sin(theta + (pi / 2)) / 2 + .5) + dy)
    d1 = (500 + scale * (cos(theta) * (sqrt(3) / 2)) + dx, 500 + -scale * (sin(theta) / 2 + .5) + dy)

    a2 = (500 + scale * (cos(theta + (3 * pi / 2)) * (sqrt(3) / 2)) + dx, 500 + -scale * (sin(theta + (3 * pi / 2)) / 2 - .5) + dy)
    b2 = (500 + scale * (cos(theta + (pi)) * (sqrt(3) / 2)) + dx, 500 + -scale * (sin(theta + (pi)) / 2 - .5) + dy)
    c2 = (500 + scale * (cos(theta + (pi / 2)) * (sqrt(3) / 2)) + dx, 500 + -scale * (sin(theta + (pi / 2)) / 2 - .5) + dy)
    d2 = (500 + scale * (cos(theta) * (sqrt(3) / 2)) + dx, 500 + -scale * (sin(theta) / 2 - .5) + dy)

    if theta < 3 * pi / 4 or theta > 7 * pi / 4: pygame.draw.polygon(win, (255, 0, 0), (a2, b2, b1, a1))
    if theta > pi / 4 and theta < 5 * pi / 4: pygame.draw.polygon(win, (255, 255, 0), (b2, c2, c1, b1))
    if theta > 3 * pi / 4 and theta < 7 * pi / 4: pygame.draw.polygon(win, (0, 255, 0), (c2, d2, d1, c1))
    if theta > 5 * pi / 4 or theta < pi / 4: pygame.draw.polygon(win, (0, 0, 255), (d2, a2, a1, d1))

    # Top Face
    pygame.draw.polygon(win, (0, 255, 255), (a1, b1, c1, d1))