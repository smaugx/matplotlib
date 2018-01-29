#!/usr/bin/env python
# -*- noplot -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



x = plt.xlim(5,5)
y = plt.xlim(0,10)

plt.plot(x,y,'r-',linewidth = 4)
plt.xlabel('x')
plt.title('test')
plt.text(4,5,"hello",fontsize = 11, va = 'top')
plt.show()

