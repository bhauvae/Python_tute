import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.hist(np.random.randn(50),bins=20,color="black",alpha=0.5)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30),color="black")
ax3.plot(np.random.randn(50).cumsum(), 'k--')

plt.show()