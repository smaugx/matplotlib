#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
#from matplotlib.pyplot  import savefig
plt.switch_backend('agg')

n = 100

for color in ['red','blue','green']:
    x,y=np.random.rand(2,n)
    scale=100*np.random.rand(n)
    plt.scatter(x,y,c=color,s=scale,label=color,alpha=0.6,edgecolors='white')

plt.title('Scatter')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
#savefig('/home/niki/sharedmac/2dSandiantu.png')

