from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from numpy import *

class PLY:
    def __init__(self, filename):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.faces = []
        self.intensidade = []
        self.confidence = []

        file = open(filename, "r")
        f = file.readlines()

        x = 99999999999999
        y = 99999999999999
        o = 99999999999999
        for i in range(len(f)):
            if 'element vertex' in f[i]:
                k = f[i].split()
                x = int(k[2])
            if 'element face' in f[i]:
                k = f[i].split()
                y = int(k[2])
            if f[i].startswith('end'):
                o = i+1
            if i >= o and i < o+x:
                vertice = f[i].split()
                self.vertices.append([float(vertice[0]), float(vertice[1]), float(vertice[2])])
                self.intensidade.append(float(vertice[4]))
                self.confidence.append(float(vertice[3]))
            elif i >= o+x and i <= o+x+y:
                face = f[i].split()
                self.faces.append([int(face[1]), int(face[2]), int(face[3])])
        self.gl_list = glGenLists(1)
        print(len(self.vertices))
        glNewList(self.gl_list, GL_COMPILE)
        glBegin(GL_TRIANGLES)
        for face in self.faces: 
            glNormal3fv(calculaNormalFace(self.vertices[face[0]], self.vertices[face[1]], self.vertices[face[2]]))
            for i in range(3):
                print(self.intensidade[face[i]])
                glColor3f(1*self.confidence[face[i]], 1*self.confidence[face[i]], 1*self.confidence[face[i]])
                glVertex3fv(self.vertices[face[i]])
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glEndList()
 
def calculaNormalFace(v0, v1, v2):
    x = 0
    y = 1
    z = 2
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    print(N[x]/NLength, N[y]/NLength, N[z]/NLength)
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)