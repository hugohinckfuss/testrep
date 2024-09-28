import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
beta = 5184000*(0.138*10**(-6))
b = 0.138*10e-6 * 5184000
x = np.linspace(0,3,100)
f = (35)*erf(x/(2*np.sqrt(beta))) - 15

plt.plot(x,f)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth= 0.5)
plt.axvline(0, color='black', linewidth= 0.5)
plt.show()