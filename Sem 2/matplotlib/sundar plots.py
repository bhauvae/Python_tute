# %%
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
ax.set_xticks([0, 250, 500, 750, 1000])
ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'])
ax.set_title('plot ka naam')
ax.set_xlabel('x ka label')
ax.set_ylabel('y ka label')

plt.show()
# %%
