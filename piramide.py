from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

vertices = (
    ( 0, 1, 0),
    ( 0.5, 0, 0.5),
    (-0.5, 0, 0.5),
    ( 0.5, 0,-0.5),
    (-0.5, 0,-0.5),
    )

linhas = (
    (0,1),
    (0,2),
    (0,3),
    (0,4),
    (1,2),
    (1,3),
    (2,4),
    (3,4),
    )

facesQuad = (1,2,4,3)
faces = (
    (0,1,3),
    (0,1,2),
    (0,2,4),
    (0,3,4),
    )

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
corBase = ((1,1,1))

def Piramide():
    glBegin(GL_TRIANGLES)
    i = 0
    for face in faces:
        glColor3fv(cores[i])
        for vertex in face:
            #glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glBegin(GL_QUADS)
    for vertex in facesQuad:
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
glutCreateWindow("Piramide")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(25,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,0,0,0)
glutTimerFunc(50,timer,1)
glutMainLoop()