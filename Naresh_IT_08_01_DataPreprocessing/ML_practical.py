import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\08_NARESH_IT_MACHINE_LEARNING\Naresh_IT_08_01_MachineLearning\Data.csv")

X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values

# DATA PRE-PROCESSING
#-----------------------------------------------------------------------------

from sklearn.impute import SimpleImputer
# Simple Imputer --> Transformer for missing numerical data 

imputer = SimpleImputer(strategy='median')
# imputer = SimpleImputer()-------------------------------- mean
# imputer = SimpleImputer(strategy='mean')----------------- mean
# imputer = SimpleImputer(strategy='most_frequent')-------- mode

imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

#-----------------------------------------------------------------------------

from sklearn.preprocessing import LabelEncoder
# Label Encoder --> Transformer for categorical data 

LabelEncoder_X = LabelEncoder()
LabelEncoder_X.fit_transform(X[:,0])
X[:,0] = LabelEncoder_X.fit_transform(X[:,0])

LabelEncoder_Y = LabelEncoder()
Y = LabelEncoder_Y.fit_transform(Y)

#-----------------------------------------------------------------------------

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=0)

#_____________________________________________________________________________

# REGRESSION MODELS

# SIMPLE LINEAR REGRESSION














