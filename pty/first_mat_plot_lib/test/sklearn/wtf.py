from sklearn import datasets
from matplotlib import pyplot as plt

n_samples = 4000 # колчество точек?
n = 3 #количество классов?
x, y = datasets.make_classification(n_samples, n_classes = 3)
print(x[:,0])
plt.scatter(x[:,0], x[:,1]) # это вообще как работает

plt.show()