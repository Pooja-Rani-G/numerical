import numpy as np
import time

n=int(input('Enter position of element required'))
fib=[0,1]
t_1=time.time()
for i in range(2,n+1):
	a=fib[i-1]+fib[i-2]
	fib.append(a)
t_2=time.time()
print(fib[n])
print("time taken is equal to")
print(t_2-t_1)
