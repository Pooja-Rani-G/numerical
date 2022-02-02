import numpy as np

def f(x):
	return(np.exp(x))

l=int(input("Enter number of iterations "))
a=0
b=1
delt =(b-a)/l
suml=0
summ=0
sumr=0
for i in range(l):
	xl=a+i*delt	
	xm=a+(i+0.5)*delt
	xr=a+(i+1)*delt	
	suml+=f(xl)
	summ+=f(xm)
	sumr+=f(xr)
suml=suml*delt
summ=summ*delt
sumr=sumr*delt
print("Integration by left-point method is")
print(suml)
print("Integration by mid-point method is")
print(summ)
print("Integration by right-point method is") 
print(sumr)
print("Real value of integration is")
A=np.exp(1)-1
print(A)
errl=np.abs(A-suml)
errm=np.abs(A-summ)
errr=np.abs(A-sumr)
i=0
if errl<errm:
	if errl<errr:
		i=1
	else:
		i=3
else:
	if errm<errr:
		i=2
	else:
		i=3
if i==1:
	print("Left-point method is better")
if i==2:
	print("Mid-point method is better")
if i==3:
	print("Right-point method is better")
