
# COUNTRY GDP ANALYSIS

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

print(pd.__version__)

df = pd.read_csv(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\01_NARESH_IT_PYTHON\Naresh_IT_06_Pandas\data.csv")
print(df)
print(id(df))
print(type(df))

print(len(df))
print(df.columns)
print(len(df.columns))

df1 = df.copy()
print(df1.columns)
df1.columns = ['a','b','c','d','e']
print(df1.columns)

print(df.isnull())
print(df.isna())

print(df.isnull().sum())

print(df.head())
print(df.head(3))
print(df.head(10))
print(df.tail())

print(df.dtypes)

print(df.info())

#____________________________________________________________________________________________

# Slicing in Dataframe

# Accessing Rows
print(df[:])
print(df[::-1])
print(df[:11])
print(df[0:200:50])

# Accessing Columns
print(df['CountryName'])
print(df[['CountryName','CountryCode']])
print(df[['CountryName','CountryCode','BirthRate']])

df_categorical = df[['CountryName','CountryCode','IncomeGroup']]
print(df_categorical.head())

# MATHEMATICAL COLUMNS

print(df.BirthRate * df.InternetUsers)

# Add Column
df['MyCalc'] = df.BirthRate * df.InternetUsers
print(df)

# Deleting a Column
df = df.drop('MyCalc',axis=1)
# axis 0 = Rows, axis 1 = Columns
print(df.columns)

# CONDITIONALS
filter1= df.InternetUsers<2
print(filter1)
print(df[filter1])

filter2 = df.BirthRate>40
print(filter2)
print(df[filter2])

print(filter1 & filter2)

print(df[df.IncomeGroup=='High income'])

# How to get unique categories
print(df.IncomeGroup.nunique())
print(df.IncomeGroup.unique())

#_____________________________________________________________________________________________________________
# Descriptive Statistics (shows only numerical data)

print(df.describe())
df_cat = df[['CountryName','CountryCode','BirthRate']]
print(df_cat)
print(df_cat.describe())

# TRANSPOSE
# converts row into columns and columns into rows
print(df.describe().T)

#__________________________________________________________________________________________________________________

# ANALYZING PYTHON DATAFRAME & DATASET

print(df.head())
print(df['InternetUsers'])

# Distributions

# Univariate Analysis
# Plotting the graph using 1 variable

# distplot- distributions plot
vis1 = sns.distplot(df['InternetUsers'])
plt.show()
vis2 = sns.distplot(df['InternetUsers'], bins=15)
plt.show()

# displot- Histogram
vis3 = sns.displot(df['InternetUsers'])
plt.show()

# Bivariate Analysis
# Plotting the graph using 2 variables

# Box plot
vis4 = sns.boxplot(data=df,x='IncomeGroup',y='BirthRate')
plt.show()
vis5 = sns.boxplot(data=df,x='IncomeGroup',y='BirthRate',hue='IncomeGroup')
plt.show()
# outliers= anomaly
# 2 algorithms used for Anomaly detection (using sigmoid functions)
            # Logistic Regression
            # Naive Bayes

# Linear Model plot
vis6 = sns.lmplot(data=df,x='InternetUsers',y='BirthRate')
plt.show()
vis7 = sns.lmplot(data=df,x='InternetUsers',y='BirthRate',hue='IncomeGroup')
plt.show()
vis8 = sns.lmplot(data=df,x='InternetUsers',y='BirthRate',fit_reg=False,hue='IncomeGroup')
plt.show()                             # hue- parameter for colour
vis9 = sns.lmplot(data=df,x='InternetUsers',y='BirthRate',fit_reg=True,hue='IncomeGroup')
plt.show()