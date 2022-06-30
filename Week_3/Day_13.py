# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:40:28 2022

@author: hp
"""

"""
1. Importing the libraries
2. Importing the Dataset
3. Handling of Missing Data
4. Handling of Categorical Data
5. Splitting the Dataset in Testing and Traning
6. Feature Scaling
"""

# libraries
import numpy as np
import pandas as pd
import sklearn
# used for handling numbers
# used for handling the dataset
from sklearn.impute import SimpleImputer
# used for handling missing data
from sklearn.preprocessing import SimpleImputer,LabelEncoder, OneHotEncoder # used for encoding categorical data

# to import the dataset into variable
dataset = pd.read_csv('C:/Users/hp/Desktop/NITTTR_TRANING_2022/week_3/Book2.csv')
print(dataset)

# splitting the attributes into independent and dependent
# X = features
X = dataset.iloc[:,:-1].values # independent variables/ class
print(X)
# attribute to determine dependent variable/class
# Y = labels
Y = dataset.iloc[:,-1] # dependent variables/class
print(Y)

