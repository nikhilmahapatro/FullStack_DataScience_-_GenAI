
# COUNTRY GDP ANALYSIS

import pandas as pd
import seaborn as sns

print(pd.__version__)

df = pd.read_csv(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\01_NARESH_IT_PYTHON\Naresh_IT_06_Pandas\data.csv")
print(df)
print(id(df))
print(type(df))

print(len(df))
print(df.columns)
print(len(df.columns))

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
#_____________________________________________________________________________________________________________
# Descriptive Statistics (shows only numerical data)

print(df.describe())
df_cat = df[['CountryName','CountryCode','BirthRate']]
print(df_cat)
print(df_cat.describe())

# TRANSPOSE
# converts row into columns and columns into rows
print(df.describe().T)

