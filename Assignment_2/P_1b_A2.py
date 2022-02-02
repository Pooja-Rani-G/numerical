import numpy as np

a=-1
def f(x):
    return (np.sin(np.cos(np.exp(x))))
def g(x):
    return (-(np.sin(np.exp(x)))*(np.cos(np.cos(np.exp(x))))*(np.exp(x)))
L=int(input("Enter no. of iterations "))
for i in range(L):
    a=a-(f(a)/g(a))

print(a)

