# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:33:25 2026

@author: Rati
"""
import scipy as sc
import matplotlib.pyplot as plt
import numpy as np

#particle mass adn charge
m = 1
q = 0.2
r0=[0,0,0]
v0=[4,0,0]

#fields can be t dependent  
def B(t):
    b_x=0
    b_y=0
    b_z=1
    B=np.array([b_x,b_y,b_z])
    return B

def E(t):
    E_x=1
    E_y=-0.1
    E_z=0.01
    E=np.array([E_x,E_y,E_z])
    return E

def VDR(t):
    try:
        Vd=np.cross(E(t),B(t))/np.linalg.norm(B(t))**2
        return Vd
    except ZeroDivisionError:
        return(0)


def fun(t,y):
    Dr=y[3:]
    Dv=q*(np.array(E(t)+np.cross(Dr,B(t))))/m
    a=np.concatenate((Dr,Dv),axis=0)
    return a

t_span=[0,100]

y0=np.concatenate((r0,v0),axis=0)

solution=sc.integrate.solve_ivp(fun, t_span, y0, max_step=0.1)

print(solution)


x_trajectory = solution.y[0]
y_trajectory = solution.y[1]
z_trajectory = solution.y[2]
time=solution.t


fig = plt.figure(figsize=plt.figaspect(0.5))
ax1 = fig.add_subplot(2, 2, 1, projection='3d')


ax1.plot(x_trajectory, y_trajectory, z_trajectory, label="Particle Path",color='#990000')

ax1.set_ylabel("Y ")
ax1.set_zlabel("Z ")

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(time, x_trajectory, label="x(t)",color='#100000') #black

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(time, y_trajectory, label="y(t)")

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(time, z_trajectory, label="z(t)",color='#009900')


ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()

plt.show()