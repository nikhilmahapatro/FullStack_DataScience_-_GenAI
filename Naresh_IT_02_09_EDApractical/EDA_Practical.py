
#---------------------------------------EDA PRACTICALS--------------------------------------#

# RAW DATA

import pandas as pd
print(pd.__version__)

emp = pd.read_excel(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\02_NARESH_IT_EDA\Naresh_IT_09_EDApractical\Rawdata.xlsx")
print(emp)

print(id(emp))

print(emp.columns)
print(emp.shape)
print(emp.head())
print(emp.tail())
print(emp.info())
print(emp.isnull())
print(emp.isna())
print(emp.isnull().sum())

#_______________________________________________________________________________________________________________________

# DATA CLEANING/DATA CLEANSING

print(emp)

# Name
emp['Name'] = emp['Name'].str.replace(r'\W','',regex=True)
print(emp['Name'])

# Domain
emp['Domain'] = emp['Domain'].str.replace(r'\W','',regex=True)
print(emp['Domain'])

# Age
emp['Age'] = emp['Age'].str.extract('(\\d+)')
print(emp['Age'])

# Location
emp['Location'] = emp['Location'].str.replace(r'\W','',regex=True)
print(emp['Location'])

# Salary
emp['Salary'] = emp['Salary'].str.replace(r'\W','',regex=True)
print(emp['Salary'])

# Experience
emp['Exp'] = emp['Exp'].str.extract('(\\d+)')
print(emp['Exp'])

# Removed all noisy characters from the dataset
print(emp)

#____________________________________________________________________________________________________________________

# EDA TECHNIQUES

import numpy as np

clean_data = emp.copy()
print(clean_data)

print(emp.isnull().sum())

# MISSING VALUE TREATMENT

# replacing Null values with MEAN
clean_data['Age'] = clean_data['Age'].fillna(np.mean(pd.to_numeric(clean_data['Age'])))
print(clean_data['Age'])

# replacing Null values with MEAN
clean_data['Exp'] = clean_data['Exp'].fillna(np.mean(pd.to_numeric(clean_data['Exp'])))
print(clean_data['Exp'])

# replacing Null values with MODE
clean_data['Location'] = clean_data['Location'].fillna(clean_data['Location'].mode()[0])
print(clean_data['Location'])

# Converting object datatype to integer for Salary, Exp, Age
clean_data['Salary']= clean_data['Salary'].astype(int)
clean_data['Exp']= clean_data['Exp'].astype(int)
clean_data['Age']= clean_data['Age'].astype(int)

# Converting object datatype to categorical data for Name, Domain, Location
clean_data['Name']= clean_data['Name'].astype('category')
clean_data['Domain']= clean_data['Domain'].astype('category')
clean_data['Location']= clean_data['Location'].astype('category')

# Data cleaning complete
print(clean_data)
print(clean_data.info())

# Storing the clean data into the system
clean_data.to_csv('clean_data.csv')
import os
print(os.getcwd())

#_________________________________________________________________________________________________________________

# VISUALISATION

import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Univariate Analysis
vis1 = sns.distplot(clean_data['Salary'])
#plt.show()
vis2 = sns.displot(clean_data['Salary'])
#plt.show()

# Bivariate Analysis
vis3 = sns.lmplot(data=clean_data, x='Exp', y='Salary')
#plt.show()
vis4 = sns.lmplot(data=clean_data, x='Exp', y='Salary', fit_reg=False)
#plt.show()

#____________________________________________________________________________________________________________________

# TRANSFORMERS

print(clean_data)

# Independent varibles
X_indvar = clean_data[['Name', 'Domain', 'Age', 'Location', 'Exp']]
print(X_indvar)

# Dependent Variable
Y_depvar = clean_data[['Salary']]
print(Y_depvar)

imputation = pd.get_dummies(clean_data, dtype=int)
print(imputation)