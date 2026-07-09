# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:29:36 2026

@author: admin
"""
import scipy as sc
import numpy as np
import matplotlib.pyplot as plt

m = 1
q = 20
r0=np.array([5,5,-90])
v0=np.array([-10,10,100])


def magstr(R): #mag field only in Z direction that is independent of r
    x, y, z = R
    B0 = 1      
    alpha = 0.0005 
    Bz = B0 * (1 + alpha*z**2) #z dependet fiel or nrgligalby dependent on r when taken derivative
    dB= 2*B0*alpha*z
    return [dB,np.array([0, 0, Bz])]


def acc(v,R):
    v_xy=np.linalg.norm([v[0],v[1]])
    r_xy=np.linalg.norm([R[0],R[1]])
    F_z=-(1/2)*q*v_xy*r_xy*magstr(R)[0]  
    a_z=np.array([0,0,F_z/m]) 
    return np.array(q*np.cross(v,magstr(R)[1])/m)+a_z


def fun(t,y):
    Dr=np.array(y[3:])
    Dv=acc(y[3:] ,y[:3])
    a=np.concatenate((Dr,Dv),axis=0)
    return a

t_span=[0,4]

y0=np.concatenate((r0,v0),axis=0)

solution=sc.integrate.solve_ivp(fun, t_span, y0, max_step=0.1)

x_trajectory = solution.y[0]
y_trajectory = solution.y[1]
z_trajectory = solution.y[2]

x_last=solution.y[0][-1]
y_last=solution.y[1][-1]
z_last=solution.y[2][-1]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot(x_trajectory, y_trajectory, z_trajectory, label="Particle Path")

ax.plot(x_last,y_last,z_last,'ro')
ax.plot(5,5,-90,'ro')
ax.set_xlabel("X position")
ax.set_ylabel("Y position")
ax.set_zlabel("Z position")
ax.legend()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    