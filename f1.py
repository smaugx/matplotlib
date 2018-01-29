#!/usr/bin/env python
# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt   
from matplotlib import animation   
import numpy as np
  
#first set up the figure, the axis, and the plot element we want to animate   
fig = plt.figure() 
ax1 = fig.add_subplot(1,1,1,xlim=(0, 2), ylim=(-4, 4))
line, = ax1.plot([], [], lw=2)  
def init():  
	line.set_data([], [])  
	return line

# animation function.  this is called sequentially   
def animate(i):

	x = np.linspace(0, 2 * np.pi , 1000)   
	y = np.sin(2 * np.pi * (x - 0.01 * i))  
	line.set_data(x, y)	  
	return line

anim1=animation.FuncAnimation(fig, animate, init_func=init,  frames=100, interval=5)  
plt.show()

