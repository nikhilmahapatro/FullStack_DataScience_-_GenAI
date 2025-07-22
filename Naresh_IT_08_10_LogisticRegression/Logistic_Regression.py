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











