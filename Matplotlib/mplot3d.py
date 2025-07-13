# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:36:30 2023

@author: HP
"""

#from mpl_toolkits import mpolt3d
import matplotlib.pyplot as plt
import numpy as np
ax = plt.axes(projection='3d')
z = np.random.randint(1,10,10)
x = np.random.randint(1,100,10)
y = np.random.randint(1,50,10)
plt.xlabel('x axis')
plt.ylabel('y axis')

#ax.plot3D(x,y,z,'red')
#ax.set_title('3D line plot')
#plt.show()

#ax.scatter3D(x,y,z,'red')
#plt.show()

xlist=np.linspace(-6,6,30)
ylist=np.linspace(-6,6,30)

X,Y = np.meshgrid(xlist,ylist)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X,Y,Z,cmap='Accent')
#ax.contour3D(X,Y,Z,50,cmap='Accent')
plt.show()  