import matplotlib
import matplotlib.pyplot as plt
import numpy as np 

x1 = np.arange(-1.0, 1.0, 0.005)
y1 = 7 * np.power(x1,2) - 3

x2 = np.arange(-1.0, 1.0, 0.005)
y2 = np.power(x2,5) 

fig, ax = plt.subplots()
ax.plot(x1,y1)
ax.plot(x2,y2)
ax.set(xlabel='x', ylabel='y')
ax.grid()
plt.show()