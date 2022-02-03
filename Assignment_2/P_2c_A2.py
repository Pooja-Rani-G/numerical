import numpy as np 
import matplotlib.pyplot as plt
 
err_l=[]
err_m=[]
err_r=[]
err_t=[]
err_s=[]
A=[]
left=[]
right=[]
mid=[]
simp=[]
trap=[]
def f(x):
	return(np.exp(x))

S=[]
a=0
b=1
L=int(input("Enter number of intervals "))
for j in range(L):
	delt=(b-a)/(j+1)
	suml=0
	summ=0
	sumr=0
	sumt=0
	sums=-f(a)+f(b)
	for i in range(j+1):
		suml+=delt*f(a+i*delt)
		summ+=delt*f(a+(i+0.5)*delt)
		sumr+=delt*f(a+(i+1)*delt)
		sumt+=delt*(f(a+i*delt)+f(a+(i+1)*delt))/2
		if (j+1)%2==0:
			if i%2==0:
				sums+=2*f(a+i*delt)
			else:
	
				 sums+=4*f(a+i*delt)
	if (j+1)%2==0:
		simp.append(delt*sums/3)
	left.append(suml)
	mid.append(summ)
	right.append(sumr)
	trap.append(sumt)
for i in range(L-1):
	err_l.append(left[i+1]-left[i])
	err_m.append(mid[i+1]-mid[i])
	err_r.append(right[i+1]-right[i])
	err_t.append(trap[i+1]-trap[i])
	A.append(i+1)
for i in range(len(simp)-1):
	err_s.append(simp[i+1]-simp[i])
	S.append(2*(i+1))
plt.grid()
plt.plot(A,err_l,label="Left-point Method")
plt.plot(A,err_m,label="Mid-point Method")
plt.plot(A,err_r,label="Right-point Method")
plt.plot(A,err_t,label="Trapezoidal Method")
plt.plot(S,err_s,label="Simpson Method")
plt.legend()
plt.xlabel("Itterations---->")
plt.ylabel("error---->")
plt.title("Error V/S Itterations")
plt.show()
