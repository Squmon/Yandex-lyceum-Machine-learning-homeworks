import pandas as pd

df = pd.read_csv('./social_net_stats.csv')
A = df[df.subscriptions >= 2]
B = A[A.likes >= 3]
print(B['views'].mean())