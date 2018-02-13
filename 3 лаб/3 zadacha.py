import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 25, 0.01)
y = [i * 3 + 5 for i in x]
plt.plot(x, y, 'r')
plt.show()
