import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.random.randn(30).cumsum(), 'ko--')

data = np.random.randn(30).cumsum()
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
plt.legend(loc='best')
plt.show()