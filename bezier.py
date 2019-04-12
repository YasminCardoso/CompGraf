from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random

p1x = 0
p1y = -1
p2x = 2
p2y = 0
p3x = 0
p3y = 1

def Bezier():
    teta = 0
    while teta < 2*math.pi:
        t = 0
        glBegin(GL_LINE_STRIP)
        x = p2x*math.cos(teta)
        y = p2y
        z = p2x*math.sin(teta)
        #glVertex3f(x,y,z)
        teta += math.pi/10
        while t < 1: 
            ax = p1x + t*(p2x-p1x)
            bx = p2x + t*(p3x-p2x)
            cx = ax + t*(bx-ax)
            ay = p1y + t*(p2y-p1y)
            by = p2y + t*(p3y-p2y)
            cy = ay + t*(by-ay)
            glVertex3f(cx*math.cos(teta),cy, cx*math.sin(teta));
            t += 0.1
        glEnd()
    
    
    
def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,1,0,0)
    Bezier()
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
    
#PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Bezier")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
#glRotatef(0,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()


