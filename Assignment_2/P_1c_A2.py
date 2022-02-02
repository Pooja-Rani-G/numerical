import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.sin(np.cos(np.exp(x))))
def g(x):
    return (-(np.sin(np.exp(x)))*(np.cos(np.cos(np.exp(x))))*(np.exp(x)))

v_n=[]
v_b=[]
L=int(input("Enter number of iterations "))
for j in range(L):
	b1=-1
	b2=1
	b3=(b1+b2)/2
	n=-1
	for i in range(j):
		b3=(b1+b2)/2
		by3=np.sin(np.cos(np.exp(b3)))
		by1=np.sin(np.cos(np.exp(b1)))
		by2=np.sin(np.cos(np.exp(b2)))
		if by1*by3>0:
			b1=b3
		if by2*by3>0:
			b2=b3
		n=n-(f(n)/g(n))

	v_n.append(n)
	v_b.append(b3)
err_b=[]
err_n=[]
I=[]
for i in range(L-1):
	diffb=v_b[i+1]-v_b[i]
	err_b.append(diffb)
	diffn=v_n[i+1]-v_n[i]
	err_n.append(diffn)
	I.append(i+1)
plt.plot(I,err_b,label="Bisection Method")
plt.grid()
plt.plot(I,err_n,label="Newton Raphson Method")
plt.xlabel("Itteration no.---->")
plt.ylabel("Error---->")
plt.legend()
plt.title("Error v/s Itteration for Bisection and Newton Raphson") 
plt.show()
