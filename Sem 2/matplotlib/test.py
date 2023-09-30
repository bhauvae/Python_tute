# %%
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
c1 = fig.add_subplot(2, 2, 1)
c1.plot(np.random.randn(100), "k-")
c2 = fig.add_subplot(2, 2, 2)
c2.hist(np.random.randn(100), bins=20, color="black", alpha=1)
c3 = fig.add_subplot(2, 2, 3)
c3.scatter(x=np.random.randn(100), y=np.random.randn(100))
# %%
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50)

fig.subplots_adjust(wspace=0, hspace=0)
# %%
fig, plots = plt.subplots(1, 1)
data = np.random.randn(20)
plots.plot(data, color="black", linestyle="-", label="default")
plots.plot(data, color="black", linestyle="--", drawstyle="steps", label="steps")
plots.legend(loc="best")
# %%
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(100).cumsum())
ax.set_title("graph ka nam")
ax.set_xlabel("x ka label")
ax.set_ylabel("y ka label")
ax.set_xlim([0, 100])
ax.set_xticks(range(0, 101, 10))
ax.set_ylim([-5, 5])
ax.set_yticks(range(-5, 6))
# %%
fig, axes = plt.subplots(1, 1)
axes.plot(np.random.randn(5000), linestyle="-", alpha=1, label="one")
axes.plot(np.random.randn(5000), linestyle=":", alpha=0.9, label="two")
axes.plot(np.random.randn(5000), linestyle="--", alpha=0.8, label="three")
axes.legend(loc="best")
plt.show()
# %%
