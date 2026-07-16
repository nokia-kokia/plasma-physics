# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:29:36 2026

@author: admin
"""
import scipy as sc
import numpy as np
import matplotlib.pyplot as plt

m = 0.2
q = 20
r0=np.array([5,5,-90])
v0=np.array([1,0,0])

x_center=[]
y_center=[]
z_center=[]

def magstr(R): 
    x, y, z = R
    alpha = 0.0005 
    Bz =-1*alpha*y**2
    return np.array([0, 0, Bz])


def acc(v,R):
    return np.array(q*np.cross(v,magstr(R))/m)


def fun(t,y):
    Dr=np.array(y[3:])
    Dv=acc(y[3:] ,y[:3])
    a=np.concatenate((Dr,Dv),axis=0)
    
    x_center.append(Rc(y[3:] ,y[:3])[0])
    y_center.append(Rc(y[3:] ,y[:3])[1])
    z_center.append(Rc(y[3:] ,y[:3])[2])
    
    return a

def Rc(v,R):
    ac=acc(v,R)
    R_c=R+np.linalg.norm(v)**2*ac/np.linalg.norm(ac)**2
    return R_c
    
    
    
t_span=[0,15]

y0=np.concatenate((r0,v0),axis=0)

solution=sc.integrate.solve_ivp(fun, t_span, y0, max_step=0.1)

time=np.array(solution.t)
x_trajectory = np.array(solution.y[0])
y_trajectory = np.array(solution.y[1])
z_trajectory = np.array(solution.y[2])


x_last=solution.y[0][-1]
y_last=solution.y[1][-1]
z_last=solution.y[2][-1]


   
x_trajectory = solution.y[0]
y_trajectory = solution.y[1]
z_trajectory = solution.y[2]
time=solution.t


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


guiding_c=(max(y_trajectory)+min(y_trajectory))/2


ax.plot(x_trajectory, y_trajectory, z_trajectory, label="Particle Path")
ax.plot( x_center, y_center,z_center, label="inst. center",color='#009900')
ax.plot( x_center, np.zeros(len(x_center))+guiding_c,z_center, label="guiding center",color='#000090')


ax.plot(x_last,y_last,z_last,'ro')
ax.plot(5,5,-90,'ro')
ax.set_xlabel("X position")
ax.set_ylabel("Y position")
ax.set_zlabel("Z position")
ax.legend()
    

    
    
    
    
    
    
    
    
    
    