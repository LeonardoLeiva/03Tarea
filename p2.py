import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D

'''
Resuelve el sistema de lorentz por medio de RK4 de scipy.integrate. grafica en
3d los valores obtenidos para las variables 'z', 'y' y 'z'. con los parametros
usados se obtendra el atractor de lorentz
'''
#crea figuras

fig=plt.figure(1)
fig.clf()
ax=fig.add_subplot(111,projection='3d')
ax.set_aspect('equal')

#parametros
o=10
b=8/3.
rho=28

#funciones

dx= lambda x,y,z: (o*(y-x))
dy= lambda x,y,z: (x*(rho-z)-y)
dz= lambda x,y,z: (x*y-b*z)

#func= lambda x,y,z: dx,dy,dz #se intento implementar de este modo, pero no
#funciona. Se propone buscar agregar el parametro 't', pero queda pendiente

def func(t,var):
    x,y,z=var #'var' debe incluir las coordenadas en 3 dimensiones
    xd=dx(x,y,z) #evalua los valores entregados para cada coordenada
    yd=dy(x,y,z)
    zd=dz(x,y,z)
    return [xd,yd,zd]

#condiciones iniciales
x0=5; y0=8; z0=-1; t0=0
ci=[x0,y0,z0] #crea un vector con los valores iniciales para ser consecuentes
#con ingresar las condiciones iniciales juntas en la funcion definida


r=ode(func)
#se fijo un paso maximo porque el programa entregaba advertencia de que el paso
#se volvia muy pequeño (UserWarning: dopri5: step size becomes too small)
r.set_integrator('dopri5',max_step=0.01)
r.set_initial_value(ci,t0)

#t=np.linspace(t0,35,10000) #se recomienda ver el grafico en tf=35
t=np.linspace(t0,80,10000)
#se escoge tf=80 porque para valores mayores el grafico solo se vuelve más
#denso, pero no se aleja de los atractores

#arreglos para x, y, z. es mas compacto que usar listas y la funcion 'append'
x=np.zeros(len(t))
y=np.zeros(len(t))
z=np.zeros(len(t))

for i in range(len(t)):
    r.integrate(t[i])
    x[i],y[i],z[i]=r.y

ax.plot(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('Atractor de Lorentz en 3-Dim')
plt.show()

#print x
#print y
#print z
