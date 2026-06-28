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
v0=[0,0,0]
r0=[1,2,3]

#fields can be t dependent  
def B(t):
    b_x=0.0001*t
    b_y=0
    b_z=5
    B=[b_x,b_y,b_z]
    return B

def E(t):
    E_x=0
    E_y=0
    E_z=1
    E=[E_x,E_y,E_z]
    return E


def fun(t,y):
    Dr=y[3:]
    Dv=q*(np.array(E(t)+np.cross(Dr,B(t))))/m
    a=np.concatenate((Dr,Dv),axis=0)
    return a

t_span=[0,100]

y0=np.concatenate((v0,r0),axis=0)

solution=sc.integrate.solve_ivp(fun, t_span, y0, max_step=0.1)

x_trajectory = solution.y[0]
y_trajectory = solution.y[1]
z_trajectory = solution.y[2]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot(x_trajectory, y_trajectory, z_trajectory, label="Particle Path")


ax.set_xlabel("X position")
ax.set_ylabel("Y position")
ax.set_zlabel("Z position")
ax.legend()

plt.show()