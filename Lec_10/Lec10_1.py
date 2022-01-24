import numpy as np

x=[0,1,2]
y=[1,2,4]
a=1.5
sum=0
for i in range(3):
        L=1
        for j in range(3):
                if j!=i:
                        L=L*(a-x[j])/(x[i]-x[j])
        sum=sum+L*y[i]
print("Value at 1.5 is")
print(sum)
val=2**(1.5)
print("Real  value is")
print(val)
err=val-sum
print("Error is")
print(err)

