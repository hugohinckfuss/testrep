# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: -1*np.sin(2*x) + 1.25*x - 0.75
# fixed point is alpha1 = 1.4987....

     #f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-11

# test f1 '''
     x0 = np.pi/2
     [xstar,ier, x, count] = fixedpt(f1,x0,tol,Nmax)
     [alpha, _lambda] = compute_order(x, xstar)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
     print(f"lambda is {_lambda}")
     print(f"alpha is {alpha}")
     print(f"count is {count}")
    
#test f2 '''
     #x0 = 0.0
     #[xstar,ier] = fixedpt(f2,x0,tol,Nmax)
     #print('the approximate fixed point is:',xstar)
     #print('f2(xstar):',f2(xstar))
     #print('Error message reads:',ier)



# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    x = []

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier, x, count]
       x0 = x1
       x.append(x1)

    xstar = x1
    ier = 1
    return [xstar, ier, x, count]
    
def compute_order(x, xstar):

# x_n+1 - x*
     diff1 = np.abs(np.array(x[1:-1]) - xstar)
# x_n - x*
     diff2 = np.abs(np.array(x[:-2]) - xstar)

     fit = np.polyfit(np.log(diff2.flatten()), np.log(diff1.flatten()),1)
     _lambda = np.exp(fit[1])
     alpha = fit[0]

     return fit

driver()