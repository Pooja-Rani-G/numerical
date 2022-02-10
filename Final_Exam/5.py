import numpy as np

L=400
xa=-1
xb=1
ya=-1
yb=1
xbin=(xb-xa)/L
ybin=(yb-ya)/L
def f(x,y):
	return(np.sqrt(4-x**2-y**2))
sum=0
for i in range(L):
	for j in range(L):
		sum+=f(xa+(i+0.5)*xbin,ya+(j+0.5)*ybin)*xbin*ybin
print(sum)
				
