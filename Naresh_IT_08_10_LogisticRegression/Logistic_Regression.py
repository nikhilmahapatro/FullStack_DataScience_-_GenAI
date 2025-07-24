#----------------------------CLASSIFICATION MODELS---------------------------#

# LOGISTIC REGRESSION

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\08_NARESH_IT_MACHINE_LEARNING\Naresh_IT_08_10_LogisticRegression\logit classification.csv")

X = dataset.iloc[:,[2,3]].values
Y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.20, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
CM = confusion_matrix(Y_test, Y_pred) 
print(CM)

from sklearn.metrics import accuracy_score
acc = accuracy_score(Y_test, Y_pred) 
print(acc)

from sklearn.metrics import classification_report
CR = classification_report(Y_test, Y_pred)
print(CR)

bias = classifier.score(X_train, Y_train)
print(bias)
variance = classifier.score(X_test, Y_test)
print(variance)

# acc= 92.5, bias=82, var= 92.5..................best fit model


# FUTURE PREDICTIONS --------------------------

dataset1 = pd.read_csv(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\08_NARESH_IT_MACHINE_LEARNING\Naresh_IT_08_10_LogisticRegression\Future prediction1.csv")

d2 = dataset1.copy()

dataset1 = dataset1.iloc[:, [2, 3]].values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
M = sc.fit_transform(dataset1)

y_pred1 = pd.DataFrame()

d2 ['y_pred1'] = classifier.predict(M)

d2.to_csv('final1.csv')

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, Y_set = X_train, Y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(Y_set)):
    plt.scatter(X_set[Y_set == j, 0], X_set[Y_set == j, 1],
                c = ListedColormap(('blue', 'yellow'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, Y_set = X_test, Y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(Y_set)):
    plt.scatter(X_set[Y_set == j, 0], X_set[Y_set == j, 1],
                c = ListedColormap(('blue', 'yellow'))(i), label = j)
plt.title('Logistic Regression (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()



