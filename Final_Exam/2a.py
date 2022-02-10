import numpy as np

r=10 
def y(x):
	return(np.sqrt(r**2-x**2))
L=400
a=-1*r
b=r
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
print(sum)
