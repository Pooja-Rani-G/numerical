import numpy as np
import matplotlib.pyplot as plt

y=np.loadtxt('data.txt')
plt.grid()
plt.scatter(y[:,0],y[:,1],c='purple',marker='*')
plt.xlabel("x----->",size=20)
plt.ylabel("y----->",size=20)
plt.title("Plotting of Data.txt",size=20)
plt.show()

