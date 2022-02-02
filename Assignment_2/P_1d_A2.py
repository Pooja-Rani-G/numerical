import numpy as np
from scipy import optimize

def f(x):
    return (np.sin(np.cos(np.exp(x))))
def g(x):
    return (-(np.sin(np.exp(x)))*(np.cos(np.cos(np.exp(x))))*(np.exp(x)))

rn=optimize.newton(f,-1,g)
print("Root by Newton Raphson Method is")
print(rn)
print("Root by Bisection Method is")
rb=optimize.bisect(f,-1,1)
print(rb)
