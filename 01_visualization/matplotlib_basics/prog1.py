import numpy as np


def MSE(o, p):  # mean sqr err
    e = o - p
    return np.sum(e * e) / len(e)


def MAE(o, p):  # mean abs err
    e = o - p
    return np.sum(np.abs(e)) / len(e)


def RMSE(o, p):  # rooted MSE
    return MSE(o, p)**0.5


tValues = np.array(eval("[" + input().replace(' ', ',') + "]"), np.float32)
pValues = np.array(eval("[" + input().replace(' ', ',') + "]"), np.float32)

print("MSE: {:.2f}".format(MSE(tValues, pValues)))
print("MAE: {:.2f}".format(MAE(tValues, pValues)))
print("RMSE: {:.2f}".format(RMSE(tValues, pValues)))
