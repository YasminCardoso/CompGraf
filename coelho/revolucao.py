from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
from random import *

#(r*cosA*cosP, r*senA*senP, r*cosA*senP)

r = 6

alpha = -pi/2
phi = 0

xCirculo = r*cos(alpha)*cos(phi)
yCirculo = r*sin(alpha)*sin(phi)
zCirculo = r*cos(alpha)*sin(phi)

a = 0.9
b = 0.9

x0 = -2
y0 = -2

xf = 2
yf = 2

px = 10
py = 10
vertex = []

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def revolucao():
    i = 0
    j = 0
    dx = (xf -x0)/2px
    dy = (yf -y0)/2py
    y = y0
    glPushMatrix()
    glTranslatef(0,0,6)
    while(y <= yf):
        x = x0
        glBegin(GL_QUAD_STRIP)
        while(x <= xf):
            glColor3f(uniform(0,1), uniform(0,1), uniform(0,1))
            glVertex3f(x, y, f(x,y))
            glColor3f(uniform(0,1), uniform(0,1), uniform(0,1))
            glVertex3f(x, y+dy, f(x, y+dy))
            x += dx
        y += dy
        glEnd()
    y = y0
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,0,-8)
    while(y <= yf):
        x = x0
        glBegin(GL_QUAD_STRIP)
        while(x <= xf):
            glColor3f(uniform(0,1), uniform(0,1), uniform(0,1))
            glVertex3f(x,y,f2(x,y))
            glColor3f(uniform(0,1), uniform(0,1), uniform(0,1))
            glVertex3f(x,y+dy,f2(x,y+dy))
            x += dx
        y += dy
        glEnd()
    glPopMatrix()

def f2 (x,y):
    return (a*x)**2 + (b*y)**2

def f (x,y):
    return -(a*x)**2 + -(b*y)**2

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,0,1,0)
    revolucao()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(5,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,800)
glutCreateWindow("REVOLUCAO DA HORA")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(50,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-20)
#glRotatef(45,0,0,0)
glutTimerFunc(50,timer,1)
glutMainLoop()