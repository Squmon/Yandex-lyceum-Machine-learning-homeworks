from matplotlib import pyplot as plt
import numpy as np



image = np.eye(100) + np.eye(100)[::-1]

plt.imshow(image)
plt.show()