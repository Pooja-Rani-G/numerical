import numpy as np
	
l=int(input("Enter length of array "))
arr=[]
for i in range(0,l):
	a=float(input('Enter element '))
	arr.append(a)
n=int(input('Enter n(for top n)'))
for t in range(0,n):
	g=arr[t]
	j=t
	for i in range(t,l):
		if g<arr[i]:
			g=arr[i]
			j=i
	s=arr[j]
	arr[j]=arr[t]
	arr[t]=s
for t in range(0,n):
	print(arr[t])
