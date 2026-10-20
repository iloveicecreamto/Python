# Implementation of at least one classification algorithm using scikit-learn. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from matplotlib.colors import ListedColormap
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()

X = iris.data[:,[2,3]]
Y = iris.target

print(X[1:5,:])
print(Y)
plt.figure(2, figsize=(8, 6))
plt.clf() #clear figure

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.show()
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=0)
length_Train = len(X_train)
length_Test = len(X_test)
print("There are ",length_Train,"samples in the trainig set and",length_Test,"samples in the test set")
print("-----------------------------------------------------------------------------------------------")
print("")
sc = StandardScaler()
sc.fit(X_train)
X_train_standard = sc.transform(X_train)
X_test_standard = sc.transform(X_test)
print("X_train without standardising features")
print("--------------------------------------")
print(X_train[1:5,:])
print("")
print("X_train standardising features")
print("--------------------------------------")
print(X_train_standard[1:5,:])
def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    color_Map = ListedColormap(colors[:len(np.unique(y))])
    x1_min = X[:, 0].min() - 1
    x1_max = X[:, 0].max() + 1
    x2_min = X[:, 1].min() - 1
    x2_max = X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))

    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contour(xx1, xx2, Z, alpha=0.4, cmap=color_Map)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # Plot samples
    X_test, Y_test = X[test_idx, :], y[test_idx]

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=color_Map(idx),
                    marker=markers[idx], label=cl
                    )

X_combined_standard = np.vstack((X_train_standard,X_test_standard))
Y_combined = np.hstack((Y_train, Y_test))
lr = LogisticRegression(C = 1000.0, random_state = 5 )
print(lr.fit(X_train_standard, Y_train))
Y_pred_Logit = lr.predict(X_test_standard)
print("Accuracy: %.2f" % accuracy_score(Y_test,Y_pred_Logit))
plot_decision_regions(X = X_combined_standard
                      , y = Y_combined
                      , classifier = lr
                      , test_idx = range(105,150))
plt.show()
