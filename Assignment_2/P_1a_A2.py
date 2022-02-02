import numpy as np

a=-1
b=1
xmid=(a+b)/2
ymid=np.sin(np.cos(np.exp(xmid)))
while  np.abs(ymid)>0.000001:
	ya=np.sin(np.cos(np.exp(a)))
	yb=np.sin(np.cos(np.exp(b)))
	if ya*ymid>0:
		a=xmid
	if yb*ymid>0:
		b=xmid
	xmid=(a+b)/2
	ymid=np.sin(np.cos(np.exp(xmid)))
print(xmid)

