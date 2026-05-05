from matplotlib import pyplot as plt
import numpy as np

x_plot = np.arange(-5, 5, 0.1)
y_plot = np.sin(x_plot)

x_scatter = np.arange(-5, 5, 0.1)
y_scatter = np.sin(x_scatter)

plt.plot(x_plot, y_plot)
plt.scatter(x_scatter, y_scatter, c = 'red', marker='^')

plt.show()