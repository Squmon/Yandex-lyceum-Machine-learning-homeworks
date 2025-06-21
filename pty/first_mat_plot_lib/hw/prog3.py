import pandas as pd
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


pg = pd.read_csv('./penguins.csv')
pg = pg.dropna()


labels = pg['species'].to_numpy()
features = pg[['bill_length_mm', 'bill_depth_mm']].to_numpy()


train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, test_size=0.2, random_state=123)

accurs = []
for n in range(1, 11):
    for wval in ['uniform', 'distance']:
        knn = KNeighborsClassifier(n_neighbors=n, weights=wval)
        knn.fit(train_features, train_labels)
        accurs.append(metrics.accuracy_score(
            knn.predict(test_features), test_labels))

print('Best accuracy: {:.6f}'.format(max(accurs)))
print('Worst accuracy: {:.6f}'.format(min(accurs)))
