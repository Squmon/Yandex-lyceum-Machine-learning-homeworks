import numpy as np


def minmax_scale(X: np.ndarray):
    if len(X) <= 1:
        return np.zeros_like(X, np.float32)
    Mi = X.min(axis=0)
    Ma = X.max(axis=0)
    return (X - Mi) / (Ma - Mi)


X = np.array([])
print(minmax_scale(X))
