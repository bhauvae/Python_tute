# %%
import matplotlib.pyplot as plt
from numpy.random import randn
fig = plt.figure(); ax = fig.add_subplot(1, 1, 1)

ax.plot(randn(100).cumsum(), 'k', label='one')
ax.plot(randn(100).cumsum(), 'k--', label='two')
ax.plot(randn(100).cumsum(), 'k.', label='three')
ax.legend(loc='best')
plt.show()


# %%
