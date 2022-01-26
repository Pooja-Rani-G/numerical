import numpy as np
import matplotlib.pyplot as plt
mu=0
sigma=1
x=np.random.normal (mu, sigma, 1000)
plt.hist(x, range=(-2,2) , color='purple')
plt.grid()
plt.title( 'Histogram for Gaussian Distribution')
plt.xlabel(" Numbers")
plt.ylabel ( 'Frequencv')
plt.show()
