import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = load_iris(return_X_y=True)
X = X[:, 2:4]  # petal length, petal width
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

sc = StandardScaler().fit(X_train)
lr = LogisticRegression(C=1000.0, random_state=5).fit(sc.transform(X_train), y_train)
print("Accuracy: %.2f" % accuracy_score(y_test, lr.predict(sc.transform(X_test))))

X_all = sc.transform(np.vstack((X_train, X_test)))
y_all = np.hstack((y_train, y_test))
cmap = ListedColormap(('red', 'blue', 'lightgreen'))
xx, yy = np.meshgrid(np.arange(X_all[:, 0].min() - 1, X_all[:, 0].max() + 1, 0.02),
                     np.arange(X_all[:, 1].min() - 1, X_all[:, 1].max() + 1, 0.02))
Z = lr.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contour(xx, yy, Z, alpha=0.4, cmap=cmap)
for i, c in enumerate(np.unique(y_all)):
    plt.scatter(*X_all[y_all == c].T, c=[cmap(i)], marker='so^'[i], alpha=0.8)
plt.xlabel('Petal length (standardized)')
plt.ylabel('Petal width (standardized)')
plt.show()