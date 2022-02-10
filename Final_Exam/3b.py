import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

y=np.loadtxt('data.txt')
plt.grid()
A=interpolate.CubicSpline(y[:,0],y[:,1])
x=np.linspace(-2,2,200)
plt.plot(x,A(x),color='green')
plt.xlabel("x----->",size=20)
plt.ylabel("y----->",size=20)
plt.title("Plotting of Data.txt",size=20)
plt.show()
