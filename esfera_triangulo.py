from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random

a0 = (-math.pi)/2
af = (math.pi)/2
p0 = 0
pf = (2*math.pi)
r = 3

def px(a):
    return r*math.cos(a)

def py(a):
    return r*math.sin(a)

def qx(r2,p):
    return r2*math.cos(p)
    
def qz(r2,p):
    return r2*math.sin(p)

def EsferaTriangulo():
    a = a0
    glBegin(GL_TRIANGLES)
    while a < af:
        aAux = a + (math.pi/10)
        glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
        p = p0
        while p < pf:
            pAux = p + (math.pi/10)
            l = (qx(px(a),p), py(a), qz(px(a),p))
            #print(aAux,p)
            #quit()
            q = (qx(px(aAux),p), py(aAux), qz(px(aAux),p))
            r = (qx(px(a),pAux), py(a), qz(px(a), pAux))
            s = (qx(px(aAux),pAux), py(aAux), qz(px(aAux), pAux))
            glVertex3fv(l)
            glVertex3fv(q)
            glVertex3fv(r)
            #glVertex3fv(r)
            #glVertex3fv(s)
            #glVertex3fv(q)
            p += (math.pi/19)
        a += (math.pi/19)
    glEnd()
        
        
def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    EsferaTriangulo()
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
    
#PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Esfera Triângulo")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(75,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()