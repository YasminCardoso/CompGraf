from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

print("Numero de lados: ")
r = 1;
vertices = [(0,1,0)]
linhas = []
faces = []
facesBase = []
numeroPontos = int(input())
for i in range(0,numeroPontos+1):
    x = r*cos(((2*pi)/numeroPontos)*i)
    y = 0
    z = r*sin(((2*pi)/numeroPontos)*i)
    vertices.insert(i+1,(x,y,z))
    linhas.insert(i,(0,i))
    if (i+1 < numeroPontos):
        linhas.insert(i+numeroPontos,(i,i+1))
    faces.insert(i,(0,i,i+1))
    facesBase.insert(i,i+1)

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
corBase = ((1,1,1))

def Piramide():
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        if i > 7:
            i = 0
        glColor3fv(cores[i])
        for vertex in face:
            #glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glBegin(GL_POLYGON)
    for vertex in facesBase:
        glColor3fv(corBase)
        glVertex3fv(vertices[vertex])
    glEnd()

    glVertex3fv(vertices[vertex])
    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,1,1,1)
    Piramide()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(5,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Piramide Parametrizada")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(25,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,0,0,0)
glutTimerFunc(50,timer,1)
glutMainLoop()
