
#----------------------------REGRESSION MODELS---------------------------#

# SIMPLE LINEAR REGRESSION

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\08_NARESH_IT_MACHINE_LEARNING\Naresh_IT_08_02_SimpleLinearRegression\Salary_Data.csv")

X = dataset.iloc[:,:-1]
Y = dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)

# Compare Predictions VS Actual
comparision= pd.DataFrame({'Actual':Y_test, 'Prediction':Y_pred})
print(comparision)

# Visualize the test set
plt.scatter(X_test,Y_test, color='red')
plt.plot(X_train,regressor.predict(X_train), color='blue')
plt.title("Salary VS Experience")
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

m_slope= regressor.coef_
print(m_slope)

c_intercept= regressor.intercept_
print(c_intercept)

# prediction 1
y_12 = (m_slope*12) + c_intercept
print(y_12)
    
# prediction 2
y_20 = (m_slope*20) + c_intercept
print(y_20)

Y_mean = np.mean(Y)
Y = Y[0:6]
SSR = np.sum((Y_pred-Y_mean)**2)
SSE = np.sum((Y-Y_pred)**2)
SST = SSR + SSE
R2 = 1-(SSR/SST)

# Bias
bias = regressor.score(X_train,Y_train)
print(bias)

# Variance
variance = regressor.score(X_test,Y_test)
print(variance)

from sklearn.metrics import mean_squared_error
train_mse = mean_squared_error(Y_train, regressor.predict(X_train))
test_mse = mean_squared_error(Y_test, Y_pred)

# Deployment

import pickle

# Save the trained model to disk
filename = 'Simple_Linear_Regression.pkl'

# Open a file in write-binary mode and dump the model
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)

print("Model has been pickled and saved as linear_regression_model.pkl")

import os
os.getcwd()


