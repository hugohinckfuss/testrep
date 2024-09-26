# import libraries
import numpy as np

def driver():

# use routines    
    f = lambda x: np.exp(x**2+7*x-30) - 1
    fp1 = lambda x: (2*x+7)*np.exp(x**2+7*x-30)
    fp2 = lambda x: (2*np.exp(x**2+7*x-30)+(2*x+7)**2*np.exp(x**2+7*x-30))
    a = 2
    b = 4.5
    Nmax = 100

#    f = lambda x: np.sin(x)
#    a = 0.1
#    b = np.pi+0.1

    tol = 1e-100

    [astar, count, ier] = bisection(f,fp1, fp2, a,b,tol, Nmax)

    print('the approximate root is',astar)
    print('the error message reads:',ier)
    print('f(astar) =', f(astar))
    print('count = ', count)

def newton(f,fp1,d,tol,Nmax):

  p = np.zeros(Nmax+1);
  p[0] = d
  for it in range(Nmax):
      p1 = d-f(d)/fp1(d)
      p[it+1] = p1
      if (abs(p1-d) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      d = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]


# define routines
def bisection(f,fp1,fp2, a,b,tol, Nmax):

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root, then endpoints have derivate > 1
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]
    

    count = 0
    d = 0.5*(a+b)
    while abs(((f(d)*fp2(d))/(fp1(d))**2) > 1):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
      print(d)
#      print('abs(d-a) = ', abs(d-a))
    print('count =',count)

    [p,pstar,info,it] = newton(f,fp1,d,tol,Nmax)
      
    astar = d
    ier = 0
    return [pstar, count + it, ier]
      
driver()


