#----------------------------REGRESSION MODELS---------------------------#

# SUPPORT VECTOR REGRESSION

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\08_NARESH_IT_MACHINE_LEARNING\Naresh_IT_08_06_SupportVectorRegression\emp_salary.csv")

X = dataset.iloc[:,1:2]
Y = dataset.iloc[:,2]

# Linear Regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, Y)

# Linear Regression Visualizaton 
plt.scatter(X, Y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('linear regression model (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

lin_model_pred = lin_reg.predict([[6.5]])
print(lin_model_pred)

# Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=5)                      # poly_reg = PolynomialFeatures(degree=2)
                                                             # poly_reg = PolynomialFeatures(degree=3)
                                                             # poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, Y)

lin_reg_2 = LinearRegression()

lin_reg_2.fit(X_poly, Y)

# POLYNOMIAL REGRESSION MODEL
plt.scatter(X, Y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('polymodel (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# predicton 
poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred


# SUPPORT VECTOR REGRESSION MODEL 

from sklearn.svm import SVR
svr_reg = SVR(kernel="poly",degree=4,gamma="scale",C=1.0 )
svr_reg.fit(X, Y)

svr_model_pred = svr_reg.predict([[6.5]])
print(svr_model_pred)













