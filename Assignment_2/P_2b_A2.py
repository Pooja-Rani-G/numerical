import numpy as np

a=0
b=1
l=int(input("Enter even number of iterations "))
delt=(b-a)/l
sumt=0
def f(x):
	return(np.exp(x))

sums=-f(a)-f(b)
for i in range(l):
	sumt+=f(a+i*delt)+f(a+(i+1)*delt)
	if i%2==0:
		sums+=2*f(a+i*delt)
	else:
		sums+=4*f(a+i*delt)
sumt=sumt*delt/2
print("Integration by Trapezoidal Method is")
print(sumt)	
sums=sums*delt/3
print("Integration by Simpson's Method is")
print(sums)
