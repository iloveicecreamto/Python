import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

X, _ = make_moons(200, noise=0.05, random_state=0)
db = DBSCAN(eps=0.3, min_samples=10).fit(X)
labels = db.labels_
core = np.isin(np.arange(len(X)), db.core_sample_indices_)

for k in set(labels):
    col = 'black' if k == -1 else plt.cm.Spectral(k / max(labels.max(), 1))
    m = labels == k
    plt.plot(*X[m & core].T, 'o', mfc=col, mec='k', ms=14)
    plt.plot(*X[m & ~core].T, 'o', mfc=col, mec='k', ms=6)

plt.title(f'Estimated number of clusters: {labels.max() + 1}')
plt.show()