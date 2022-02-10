import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

A=[]
r=np.linspace(5,50,10)
for j in range(10):
        def y(x):
                return(np.sqrt(r[j]**2-x**2))
        L=400
        a=-1*r[j]
        b=r[j]
        sum=y(a)+y(b)
        delt=(b-a)/L
        ##using Simpson Method
        for i in range(1,L):
                if i%2==0:
                        sum+=2*y(a+delt*i)
                else:
                        sum+=4*y(a+delt*i)
        sum=sum*delt/3
        sum=sum*2
        A.append(sum)
A13=interpolate.CubicSpline(r,A)
print(A13(13))
plt.plot(r,A13(r),'tab:purple',label='Interpolation')
plt.plot(r,A,'tab:red',label='Simpson')
plt.legend()
plt.grid()
plt.xlabel("Radius--->")
plt.ylabel("Area---->")
plt.title("Area v/s Radius")
plt.show()
