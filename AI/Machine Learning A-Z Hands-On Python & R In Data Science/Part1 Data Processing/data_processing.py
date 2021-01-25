import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import csv file
dataset = pd.read_csv("Data.csv")
# print(dataset) To see whether above is completed
# print(type(dataset)) # dataframe

# dataset.iloc[row,column]
X = dataset.iloc[:, ]