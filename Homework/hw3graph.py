import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,3*np.pi,1000)
f = x - 4*np.sin(2*x) - 3

plt.plot(x,f)
plt.axhline()
plt.show()
plt.figure()