from matplotlib import pyplot as plt


for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.grid()

plt.show()