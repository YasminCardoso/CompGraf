from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

print("Numero de lados: ")
r = 1;
vertices = []
linhas = []
faces = []
facesBase = []
facesTopo = []
numeroPontos = int(input())
for i in range(0,numeroPontos+1):
    x = r*cos(((2*pi)/numeroPontos)*i)
    y = 0
    z = r*sin(((2*pi)/numeroPontos)*i)
    vertices.insert(i+1,(x,y,z))

for i in range(0,numeroPontos+1):
    x = r*cos(((2*pi)/numeroPontos)*i)
    y = 2
    z = r*sin(((2*pi)/numeroPontos)*i)
    vertices.insert(i+numeroPontos,(x,y,z))
   
for j in range(0,numeroPontos):
    if j != numeroPontos -1:
        linhas.insert(j,(j,j+1))
    else:
        linhas.insert(j+numeroPontos,(j,0))
    linhas.insert(j+numeroPontos,(j+numeroPontos,j+numeroPontos+1))
    linhas.insert(j+numeroPontos*2,(j,j+numeroPontos))

for l in range(0, numeroPontos):
    if l == numeroPontos-1:
        faces.insert(l,(l,l+1-numeroPontos,l+1,l+numeroPontos))
        facesBase.insert(l, l)
        facesTopo.insert(l, l+numeroPontos)
        break
    facesBase.insert(l, l)
    faces.insert(l,(l,l+1,l+numeroPontos+1,l+numeroPontos))
    facesTopo.insert(l, l+numeroPontos)

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
corBase = ((1,1,1))
corTopo = ((0.5,0.5,0.5))

def Prisma():
    glBegin(GL_QUADS)
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

    glBegin(GL_POLYGON)
    for vertex in facesTopo:
        glColor3fv(corTopo)
        glVertex3fv(vertices[vertex])
    glEnd()
    

    #glVertex3fv(vertices[vertex])
    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,1,1,1)
    Prisma()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(5,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Prisma")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(25,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,0,0,0)
glutTimerFunc(50,timer,1)
glutMainLoop()