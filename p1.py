import numpy as np
import matplotlib.pyplot as plt

'''
Primer intento de implementar runge kutta
'''

m=1.622

f= lambda y,dy: ((dy),(-y-m*(y**2-1)*dy))


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

def rk3(f,yn,dyn,h):
    k_1=k1(f,yn,dyn,h)
    k_2=k2(f,yn,dyn,h)
    k_3=k3(f,yn,dyn,h)
    ym=yn+(1./6.)*(k_1[0]+4*k_2[0]+k_3[0])
    dym=dyn+(1./6.)*(k_1[1]+4*k_2[1]+k_3[1])
    return ym,dym

#Termino de definicion de funciones

#f= lambda y,dy: (-y-m*(y**2-1)*dy,dy)
y0=0.1
dy0=0
s0=0
sf=20*np.pi
n=1000
h=sf/n
s=np.linspace(s0,sf,n)
y=[]
dy=[]
y.append(y0)
dy.append(dy0)
k=[]
i=0
k.append(i)
for t in s:
    yn=y[i]
    dyn=dy[i]
    rk=rk3(f,yn,dyn,h)
    y.append(rk[0])
    dy.append(rk[1])
    i=i+1
    k.append(i)
s=np.append(s,20*np.pi)

print len(y)
print len(s)
plt.figure(1)
plt.clf()
plt.plot(y,dy)
#plt.plot(s,dy)
plt.draw()
plt.show()
