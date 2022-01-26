import numpy as np
import  matplotlib.pyplot as plt

t=np.linspace(0,2*np.pi,100)
fig,ax=plt.subplots(3,sharex=True,sharey=True)
fig.suptitle('Parametric Plots')
ax[0].plot(np.cos(t),np.sin(t),'tab:red',label='a')
ax[0].set_xlabel('cos(t)')
ax[0].set_ylabel('sin(t)')
ax[0].legend()
ax[1].plot(np.cos(3*t),np.sin(2*t),'tab:purple',label='b')
ax[1].set_xlabel('cos(3t)')
ax[1].set_ylabel('sin(2t)')
ax[1].legend()
ax[2].plot(abs(np.cos(4*t))*np.cos(t),abs(np.cos(4*t))*np.sin(t),'tab:green',label='c')
ax[2].set_xlabel('|cos(4t)|cos(t)')
ax[2].set_ylabel('|cos(4t)|sin(t)')
ax[2].legend()
plt.show()
