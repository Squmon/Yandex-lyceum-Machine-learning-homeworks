import pandas as pd
import numpy as np


n = int(input())
k = int(input())


def distance(a):
    return pow(a.dot(a), 0.5)


pg = pd.read_csv('./penguins.csv')
pg = pg.dropna()

features = pg[['bill_length_mm', 'bill_depth_mm']].to_numpy()

center = features[n]


def condition(a):
    global center
    return distance(a - center)


out = sorted(features, key=condition)[1:(k + 1)]
for g in out:
    print(g)
