import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0, 50, 1000)
y = np.random.randint(0, 50, 1000)

np.corrcoef(x, y)

plt.scatter(x, y)
plt.show()
