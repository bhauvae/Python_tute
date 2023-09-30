# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
xx, yy = np.meshgrid(x, y)
z = np.sqrt(xx**2 + yy**2)
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()

# %%
import seaborn as sns
sns.heatmap(z,cmap='gray').set_xticks(range(0,1000,100))
# %%
