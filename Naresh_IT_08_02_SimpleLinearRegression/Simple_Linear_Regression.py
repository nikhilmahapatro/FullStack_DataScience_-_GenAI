
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



