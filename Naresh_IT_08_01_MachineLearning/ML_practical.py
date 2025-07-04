import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\08_NARESH_IT_MACHINE_LEARNING\Naresh_IT_08_01_MachineLearning\Data.csv")

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values
