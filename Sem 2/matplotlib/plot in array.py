import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 3,sharex=True,sharey=True)
axes[0,1].hist(np.random.randn(500),bins=20)
plt.subplots_adjust(wspace=0,hspace=0)
plt.show()

