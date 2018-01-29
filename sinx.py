#!/usr/bin/env  python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot  import savefig


x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)
#plt.plot(x,np.sin(x),x,np.sin(2*x))
#plt.plot(x,y,marker='o',mec='b',mfc='w')
plt.plot(x,y,mec='b',mfc='w')
#plt.show() 
savefig('./sinx.png')
