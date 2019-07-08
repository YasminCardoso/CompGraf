from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import png
import random
import math
import sys

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0                     

largTaca = int(sys.argv[1]) if len(sys.argv) > 1 else 2

reader = png.Reader(filename='taca2.png')
w, h, pixels, metadata = reader.read_flat()

if(metadata['alpha']):
	bytesPerPixel = 4
else:
	bytesPerPixel = 3

def posicao(linha, coluna):
	return bytesPerPixel*(w*linha+coluna)

lista = []
for linha in range(1,h-1):
	for coluna in range(1,w-1):
		pc = posicao(linha-1,coluna)
		pb = posicao(linha+1,coluna)
		p = posicao(linha,coluna)
		pe = posicao(linha,coluna-1)
		pd = posicao(linha,coluna+1)
		dv = abs(pixels[pc]-pixels[pb])
		dh = abs(pixels[pe]-pixels[pd])
		d = int(max(dv,dh))
		if d > 10:
			lista.append(1)
			d = 255
		else:
			lista.append(0)

    #print(lista)

bordas = [[0],[0]]
states = ["FORA", "BORDAE", "DENTRO", "BORDAD"]
state = states[0]
borda = 0
while borda < (w-2):
	aux = ((w-2)*((h-2)/2)) + borda

	if state == states[0]:
		if lista[int(aux)] == 1:
			bordas[0] = borda
			state = "BORDAE"

	if state == states[1]:
		if lista[int(aux)] == 0:
			state = "DENTRO"

	if state == states[2]:
		if lista[int(aux)] == 1:
			bordas[1] = borda
			state = "BORDAD"

	if state == states[3]:
		if lista[int(aux)] == 0:
			state = "FORA"

	borda += 1

centro = (bordas[0]+bordas[1])/2

# ROTACIONANDO #
p0 = 0
pf = (2*math.pi)

def py(altura):
	return ((2.0*altura)/(h-2.0))-1.0

def px(largura):

	if largTaca == 2:
		# Vinho Branco #
		return largura/(w-2.0)

	elif largTaca >= 3:
		# Vinho Tinto #
		return (1.5*largura)/(w-2.0)

	elif largTaca <= 1:
		return (0.5*largura)/(w-2.0)

def qx(r, p):
	return r*math.cos(p)

def qy(r, p):
	return r*math.sin(p)

def Desenha():
	global xrot, yrot, zrot
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	#glBegin(GL_TRIANGLES)

	glColor3f(0.05,0.5,0.99)
	glRotatef(xrot,1.0,0.0,0.0)
	glRotatef(yrot,0.0,1.0,0.0)
	glRotatef(zrot,0.0,0.0,1.0)
	
	glBegin(GL_QUADS)
	x = 0.0
	y = (h-2)*1.0
	for linha in range(0, h-2):
		for coluna in range(int(centro), int(w-2)):
			aux2 = int(((w-2)*linha)+coluna)
			if lista[aux2] == 1:
				p = p0
				r = px(x)
				a = py(y)
				while p < pf:
					rAux = px(x + 1.0)
					aAux = py(y - 1.0)
					pAux = p + (math.pi/8)
					pAux2 = p + 2*(math.pi/8)
					l = (qx(r,p), a, qy(r,p))
					m = (qx(rAux, pAux), a, qy(rAux,pAux))
					n = (qx(r, pAux2), aAux, qy(r,pAux2))
					o = (qx(rAux, pAux), aAux, qy(rAux,pAux))
					glVertex3fv(l)
					glVertex3fv(m)
					glColor3f(1,1,1)
					glVertex3fv(n)
					glColor3f(0.05,0.5,0.99)
					glVertex3fv(o)

					p += (math.pi/10)
				break
			x += 1.0
		y -= 1.0
		x = 0.0
	
	glEnd()
	#xrot  = xrot + 0.05                # X rotation
	#yrot = yrot + 0.05                 # Y rotation
	#zrot = zrot + 0.05                 # Z rotation
	glutSwapBuffers()

def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == 'x' or tecla == 'X':
        dx = 5
        dy = 0
        dz = 0   
    elif tecla == 'y' or tecla == 'Y':
        dx = 0
        dy = 5
        dz = 0   
    elif tecla == 'z' or tecla == 'Z':
        dx = 0
        dy = 0
        dz = 5

def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        xrot -= dx                # X rotation
        yrot -= dy                # Y rotation
        zrot -= dz                     
    elif tecla == GLUT_KEY_RIGHT:
        xrot += dx                # X rotation
        yrot += dy                # Y rotation
        zrot += dz
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL DO GLUT
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow('Taça')
glutDisplayFunc(Desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(30,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(1,1,1,1)
glutTimerFunc(50,timer,1)
glutKeyboardFunc(keyPressed)
glutSpecialFunc(teclaEspecialPressionada)
glutMainLoop()



					






