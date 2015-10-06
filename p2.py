import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import ode
from mpl_toolkits.mplot3d import Axes3D

'''
Primer intento por resolver el sistema de Lorenz
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

#func= lambda x,y,z: dx,dy,dz
def func(t,var):
    x,y,z=var
    xd=dx(x,y,z)
    yd=dy(x,y,z)
    zd=dz(x,y,z)
    return [xd,yd,zd]

#condiciones iniciales
x0=5; y0=8; z0=-1; t0=0
ci=[x0,y0,z0]


r=ode(func)
#se fijo un paso maximo porque el programa entregaba advertencia de que el paso
#se volvia muy pequeño (UserWarning: dopri5: step size becomes too small)
r.set_integrator('dopri5',max_step=0.01)
r.set_initial_value(ci,t0)

#t=np.linspace(t0,35,10000) #se recomienda ver el grafico en tf=35
t=np.linspace(t0,80,10000)
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

plt.show()

#print x
#print y
#print z
