import numpy as np


def snake(m, n):
    a = np.arange(1, m * n + 1)
    q = np.arange(1, m, 2)
    a.resize(m, n)
    a[q] = a[q, ::-1]
    return a
