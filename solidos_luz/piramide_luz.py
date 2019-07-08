from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

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

#cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
#corBase = ((1,1,1))

def calculaFace(face):
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]

    U = (v2[0]-v0[0], v2[1]-v0[1], v2[2]-v0[2])
    V = (v1[0]-v0[0], v1[1]-v0[1], v1[2]-v0[2])
    N = ((U[1]*V[2]-U[2]*V[1]),(U[2]*V[0]-U[0]*V[2]),(U[0]*V[1]-U[1]*V[0]))

    TamN = sqrt(N[0]*N[0]+N[1]*N[1]+N[2]*N[2])
    return (N[0]/TamN, N[1]/TamN, N[2]/TamN)

def Piramide():
    glBegin(GL_TRIANGLES)
    for face in faces:
        glNormal3fv(calculaFace(face))
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Piramide()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,5,0,0,0,0,1,0)

def init():
    mat_ambient = (0.0, 0.0, 0.5, 1.0)
    mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (0.0, 1.0, 0.0, 1.0)
    mat_shininess = (50,)
    light_position = (0.5, 0.5, 0.5)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_FLAT)
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Piramide")
glutReshapeFunc(reshape)
glutDisplayFunc(abacaxi)
glutTimerFunc(50,timer,1)
init()
glutMainLoop()