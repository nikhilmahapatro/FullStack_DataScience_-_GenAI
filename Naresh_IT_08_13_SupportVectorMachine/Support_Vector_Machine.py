#----------------------------CLASSIFICATION MODELS---------------------------#

# SUPPORT VECTOR MACHINE

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\08_NARESH_IT_MACHINE_LEARNING\Naresh_IT_08_13_SupportVectorMachine\Social_Network_Ads.csv")

X = dataset.iloc[:,[2,3]].values
Y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.20, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the SVM model on the Training set
from sklearn.svm import SVC
classifier = SVC()
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
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

# acc= 95, bias=90.3, var= 95..................best fit model

















