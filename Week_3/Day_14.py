# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 14:34:50 2022

@author: hp
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

'''

'''

data = pd.read_csv('C:/Users/hp/Desktop/NITTTR_TRANING_2022/week_3/headbrain.csv')
# values converts it into a numpy array
x = data.iloc[:,2].values.reshape(-1,1)
# -1 means that calculation the dimension of row, but have 1 column
y = data.iloc[:,3].values.reshape(-1,1)

# sckit-learn implementation 
# Model intialization
regression_model = LinearRegression()
# Fit the data ( train the model )
regression_model.fit(x,y)
# predict
y_predicted = regression_model.predict(x)
# model evaluation
rmse = mean_squared_error(y,y_predicted)
r2 = r2_score(y,y_predicted)
# printing values
print('Slope(m) : ', regression_model.coef_)
print('Intercept(c) : ', regression_model.intercept_)
print('Root mean squared error : ',rmse)
print('R2 score : ', r2)

# ploting values
# data points
plt.scatter(x, y, s = 20)
plt.xlabel('Independent variable : x')
plt.ylabel('Dependent variable : y')
# predicted values
plt.plot(x, y_predicted, color = 'r')
plt.show()