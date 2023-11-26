import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
x_rotation = y_rotation = 0
rotation_speed = 0.2

def draw_cylinder():
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)
    gluCylinder(quadric, 1, 1, 2, 32, 32)
    
def draw_cube():
    vertices = (
        (1, -1, -1),
        (1, -1, 1),
        (-1, -1, 1),
        (-1, -1, -1),
        (1, 1, -1),
        (1, 1, 1),
        (-1, 1, 1),
        (-1, 1, -1)
    )

    edges = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7)
    )

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:  # Левая кнопка мыши
        x, y = pygame.mouse.get_rel()
        x_rotation = y * rotation_speed
        y_rotation = x * rotation_speed

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glRotatef(x_rotation, 1, 0, 0)
    glRotatef(y_rotation, 0, 1, 0)

    draw_cylinder()
    draw_cube()

    pygame.display.flip()

    pygame.time.wait(10)