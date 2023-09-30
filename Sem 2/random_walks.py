import numpy as np

position = 0
steps = 1000
tries = 10000
dist = np.random.randn(tries, steps)
steps = np.where(dist < 0, -1, 1)
print(steps)

disp = np.cumsum(steps, axis=1)
print(disp)
print(disp.min(), disp.max())
hit100 = (np.abs(disp >= 100)).any(1)
print(disp[hit100])
