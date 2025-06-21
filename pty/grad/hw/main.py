import numpy as np
h = 1e-9


def end(epsilon, x1, x2) -> bool:
    return abs(x1 - x2) < epsilon


def diff(func, point):
    return (func(point + h) - func(point)) / h


def gradient_descent(func, start_point, gamma, epsilon, steps=0):
    position = start_point
    if steps == 0:
        i = 1
        position = start_point - gamma * diff(func, start_point)
        hist = [[start_point], [position]]
        while not end(epsilon, func(hist[i][0]), func(hist[i - 1][0])):
            position -= gamma * diff(func, position)
            hist.append([position])
            i += 1
    else:
        steps += 1
        hist = np.zeros([steps, 1])
        hist[0] = start_point
        for i in range(1, steps):
            hist[i][0] = hist[i - 1][0] - gamma * diff(func, hist[i - 1])

    return np.round(hist, 3)
