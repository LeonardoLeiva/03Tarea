import numpy as np
import matplotlib.pyplot as plt

'''
Implementa un método para integrar por Runge Kutta 3 y grafica los resultados de
una EDO para ciertos valores iniciales. Grafica y(s) vs dy/ds para dichas
condiciones
'''

m=1.622 #RUT=18.668.622-5

#definicion de la funcion a integrar
f= lambda y,dy: ((dy),(-y-m*(y**2-1)*dy))

#pasos para realizar runge kutta
def k1(f,yn,dyn,h):
    fn=f(yn,dyn)
    yk1=h*fn[0]
    dyk1=h*fn[1]
    return yk1,dyk1

def k2(f,yn,dyn,h):
    k_1=k1(f,yn,dyn,h)
    fn=f(yn+k_1[0]/2.,dyn+k_1[1]/2.)
    yk2=h*fn[0]
    dyk2=h*fn[1]
    return yk2,dyk2

def k3(f,yn,dyn,h):
    k_1=k1(f,yn,dyn,h)
    k_2=k2(f,yn,dyn,h)
    fn=f(yn-k_1[0]+2*k_2[0],dyn-k_1[1]+2*k_2[1])
    yk3=h*fn[0]
    dyk3=h*fn[1]
    return yk3,dyk3

#paso de runge kutta

def rk3(f,yn,dyn,h):
    k_1=k1(f,yn,dyn,h)
    k_2=k2(f,yn,dyn,h)
    k_3=k3(f,yn,dyn,h)
    ym=yn+(1./6.)*(k_1[0]+4*k_2[0]+k_3[0])
    dym=dyn+(1./6.)*(k_1[1]+4*k_2[1]+k_3[1])
    return ym,dym

#Termino de definicion de funciones

#condiciones iniciales 1)
y0=0.1
dy0=0

s0=0 #valor inicial de la variable independiente
sf=20*np.pi #valor final de la variable independiente
n=1000
h=sf/n #paso
s=np.linspace(s0,sf,n) #arreglo var indep
#arreglos para la variable dependiente y su derivada
y1=[]
dy1=[]
y1.append(y0)
dy1.append(dy0)
i=0
for t in s: #iteracion para integrar la funcion
    yn=y1[i] #saca los valores del instante anterior para calcular el actual
    dyn=dy1[i]
    rk=rk3(f,yn,dyn,h)
    y1.append(rk[0]) #agrega valores obtenidos para y y su derivada
    dy1.append(rk[1])
    i=i+1
s=np.append(s,20*np.pi) #arregla el problema de la dimension de matrices que se
#presenta. queda pendiente una mejor manera de hacer calzar las dimensiones

#proceso para las segundas condiciones iniciales
y0=0
dy0=4
y2=[]
dy2=[]
y2.append(y0)
dy2.append(dy0)
i=0
for t in s:
    yn=y1[i]
    dyn=dy1[i]
    rk=rk3(f,yn,dyn,h)
    y2.append(rk[0])
    dy2.append(rk[1])
    i=i+1

#graficar

fig=plt.figure(1)
fig.clf()
ax1=fig.add_subplot(211)
ax1.plot(y1,dy1)
plt.title('y(s) vs dy/ds para condiciones iniciales y=0.1 dy/ds=0')
ax1.set_xlabel('y')
ax1.set_ylabel('dy/ds')
ax2=fig.add_subplot(212)
ax2.plot(y2,dy2)
plt.title('y(s) vs dy/ds para condiciones iniciales y=0 dy/ds=4')
ax2.set_xlabel('y')
ax2.set_ylabel('dy/ds')




#print len(y)
#print len(s)
#plt.figure(1)
#plt.clf()
#plt.plot(y,dy)
#plt.plot(s,dy)
plt.draw()
plt.show()
