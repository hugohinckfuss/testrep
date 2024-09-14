import numpy as np
import math

A = 0.5 * np.array([[1, 1], [1 + 10**(-10), 1 - 10**(-10)]])
B = np.array([[2 * 10**(-5)], [5 * 10**(-5)]])

A_inv = np.linalg.inv(A)

A_norm = np.linalg.norm(A, ord=2)
A_inv_norm = np.linalg.norm(A_inv, ord=2)

AB = np.matmul(A_inv,B)  # or you can use np.dot(A, B)

#print(A_norm)
#print(A_inv_norm)
#print(AB)

x = 9.999999995000000 * 10**(-10)

def taylor_approximation(x):
    return 1 + x + (x**2) / 2 + (x**3) / 6

exact_value = math.exp(x)

approx_value = taylor_approximation(x)

relative_error = abs(exact_value - approx_value) / abs(exact_value)

#print(f"{approx_value:.20f}")
#print(f"{relative_error:.20f}")

import matplotlib.pyplot as plt

t = np.arange(0, np.pi + np.pi/30, np.pi/30)
y = np.cos(t)

S = np.sum(t*y)
#print("The sum is S = ", S)

R = 1.2
dr = 0.1
f = 15
p = 0
theta = np.linspace(0,2*np.pi,100)

x = R*(1 + dr*(np.sin(f*theta)))*np.cos(theta)
y = R*(1 + dr*(np.sin(f*theta)))*np.sin(theta)

plt.figure()
plt.plot(x, y)
plt.show()

import random

d_r = 0.05
num_curves = 10
theta = np.linspace(0, 2 * np.pi, 100)

plt.figure()

for i in range(1, num_curves + 1):
    R = i
    dr = d_r
    f = 2 + i
    p = random.uniform(0, 2)

    # Parametric equations
    x = R * (1 + dr * np.sin(f * theta)) * np.cos(theta)
    y = R * (1 + dr * np.sin(f * theta)) * np.sin(theta)

    # Plot the curve
    plt.plot(x, y)


plt.show()