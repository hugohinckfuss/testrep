import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

def driver():
    # Define the function
    f = lambda x: x**6 - x - 1
    
    # Use a root-finding method to get the exact root alpha
    sol = root_scalar(f, bracket=[1, 2], method='brentq')
    alpha = sol.root
    print(f'Exact root (alpha) = {alpha:.16f}')

    # Initial guesses
    x0 = 2
    x1 = 1

    # Secant method parameters
    Nmax = 100
    tol = 1.e-13

    # Call secant method
    p, _, _ = secant(f, x0, x1, tol, Nmax)

    # Plot |x_k+1 - alpha| vs |x_k - alpha|
    plot_error(p, alpha)


def secant(f, x0, x1, tol, Nmax):
    p = np.zeros(Nmax + 1)  # Array to store approximations
    p[0] = x0
    p[1] = x1

    for it in range(1, Nmax):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        p[it + 1] = x2
        
        # Check for convergence
        if abs(x2 - x1) < tol:
            return p[:it+2], 0, it + 1  # Converged successfully

        # Update values
        x0, x1 = x1, x2

    # If we reach here, the method did not converge
    return p[:it+2], 1, Nmax  # Return as separate values


def plot_error(p, alpha):
    # Calculate |x_k - alpha| and |x_k+1 - alpha|
    errors_k = np.abs(p[:-1] - alpha)  # |x_k - alpha|
    errors_k1 = np.abs(p[1:] - alpha)  # |x_k+1 - alpha|

    # Plot on log-log axes
    plt.figure(figsize=(8, 6))
    plt.loglog(errors_k, errors_k1, 'bo-', label=r'$|x_{k+1} - \alpha|$ vs $|x_k - \alpha|$')
    plt.xlabel(r'$|x_k - \alpha|$')
    plt.ylabel(r'$|x_{k+1} - \alpha|$')
    plt.title('Error Convergence in Secant Method')
    plt.grid(True, which="both", ls="--")
    plt.legend()
    plt.show()

# Run the driver function
driver()