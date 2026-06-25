import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math


pygame.init()
pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Solar System")


glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-400, 400, -300, 300)
glMatrixMode(GL_MODELVIEW)

glClearColor(0.0, 0.0, 0.0, 1.0)  # black background


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    glClear(GL_COLOR_BUFFER_BIT)
    pygame.display.flip()
    pygame.time.wait(16)

pygame.quit()