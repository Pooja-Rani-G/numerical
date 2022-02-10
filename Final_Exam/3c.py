import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

y=np.loadtxt('data.txt')
plt.grid()
A=interpolate.CubicSpline(y[:,0],y[:,1])
a=-1
b=1
xmid=(a+b)/2
for i in range(100):
	if A(xmid)*A(a)>0:
		a=xmid
	if A(xmid)*A(b)>0:
		b=xmid
	xmid=(a+b)/2
print(xmid)
