import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, 25, 0.01)
y = [math.sin(i) for i in x]
plt.plot(x, y, 'r')
plt.show()
