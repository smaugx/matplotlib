#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import random
#from matplotlib.pyplot  import savefig
#plt.switch_backend('agg')

n = 100

#for color in ['red','blue','green']:
color =  'blue'

x = np.random.rand(500)
y = np.random.rand(500)
size = np.random.rand(500) * 50
color = np.random.rand(500)
plt.scatter(x,y,size,color)
plt.colorbar()

'''
plt.title('Scatter')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
'''

plt.show()
#savefig('/home/niki/sharedmac/2dSDTtest.png')

