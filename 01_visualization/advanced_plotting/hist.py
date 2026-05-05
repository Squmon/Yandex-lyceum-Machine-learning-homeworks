from matplotlib import pyplot as plt
import numpy as np
mu = 0
sigma = 10
values = np.random.normal(mu, sigma, 10000)

plt.hist(values, bins=50, density=True)

plt.title("Histogram")

plt.xlabel("values")

plt.show()