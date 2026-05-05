import numpy as np


def R2(o, p):  # R2
    e = o - p
    mean_true = np.sum(o) / len(o)
    mean_sq = np.sum(e * e)
    return 1 - mean_sq / np.sum((o - mean_true)**2)


tValues = np.array(eval("[" + input().replace(' ', ',') + "]"), np.float32)
pValues = np.array(eval("[" + input().replace(' ', ',') + "]"), np.float32)

print("R2: {:.2f}".format(R2(tValues, pValues)))
