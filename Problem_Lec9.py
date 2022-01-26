import numpy as np

def F(x):
	return(10-3*(x**2))
		
 
a=-1
b=3
n=4
h=(b-a)/n
I=h*(F(a)+F(b)+4*F(a+h)+2*F(a+2*h)+4*F(a+3*h))/3
print('integration is ',I)


