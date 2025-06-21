import numpy as np


def calculate(products, cook):
    g = ("Молоко, литры:", "Яйца, штуки:", "Мука, кг:")
    cook = np.array(cook)
    result = np.ceil(cook@products)
    for n in range(0, 3):
        print(f"{g[n]} {int(result[n])}")
