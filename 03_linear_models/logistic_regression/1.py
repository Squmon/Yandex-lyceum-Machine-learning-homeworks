import numpy as np


def onehot_encoding(x: np.ndarray):
    L = len(x)
    x1 = np.sort(x)
    w = {}
    N = 0
    for j in x1:
        if j not in w:
            w[j] = N
            N += 1

    f = np.eye(N, N)
    Q = np.empty([L, N], np.int32)
    for j, i in enumerate(x):
        Q[j] = f[w[i]]

    return Q
