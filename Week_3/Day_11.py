# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 13:19:05 2022

@author: hp
"""


'''
Understanding Statistics in Python
'''

# Python code to demonstrate the working of mean()
# importing ststistics to handle statistical operations

import statistics

# initializing list
li = [1, 2, 3, 3, 2, 2, 2, 1]

# Using mean() to calculate the mean of the list
print("THe average of the list ' li ' is : ")
print(statistics.mean(li))

# Python code 

# importing the statistics module
from statistics import median

#importing fraction module as fr
from fraction import Fraction as fr

data1 = (2,3,4,5,7,9,11)

data2 = (2.4, 5.1, 6.7, 8.9)

data3 = (fr(1,2), fr(44,12), fr(10,3), fr(2,3))
data3

data4 = (-5,-1,-12,-19,-3)

data5 = (-1,-2,-3,-4,4,3,2,1)

data6 = ('')

print(f"Median of data set 1 is {median(data1)}")
print(f"Median of data set 2 is {median(data2)}")
print(f"Median of data set 3 is {median(data3)}")
print(f"Median of data set 4 is {median(data4)}")
print(f"Median of data set 5 is {median(data5)}") 

# Python working with median_low() and median_high()
import statistics

set1 = [1,3,3,4,5,7]

print(f"Median of the set is {statistics.median(set1)}")
print(f"High Median of the set is {statistics.median_high(set1)}")
print(f"Low Median of the set is {statistics.median_low(set1)}")


arr = [1,2,3,4,5]
# Finding Max 
Maximum = max(arr)
#Finding min
Minimum = min(arr)
Range  = Maximum - Minimum


import numpy as np
# example 1: calculating varinace of an array
a = np.array([[1,2],[3,4]])
a
print("Variance of an array is : ", np.var(a))

#Creating an arraya using stack axis = 0 means row wise array axis = 1 means column wise array
x = np.array([10,15,7,2,16])
y = ([13,0,7,4,11])
z = np.stack((x,y),axis = 0)
i = np.stack((x,y),axis = 1)
print("Variance of x : ", x.var())
print("Variance of y : ", np.var(y))
print("Variance of z : ", z.var())
print("Variance of i : ", i.var())

"""
numpy.stack(array, axis = 0)
join a sequence of array along a new axis.

The axis parameter specifies the index of the new axis in the dimensionbs.
if axis = 0 it will be row and if axis = 1 it will be column
"""
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.stack((a,b),axis = 0))
print(np.stack((a,b),axis = 1))


# Variance 
from statistics import variance
data1 = (2,3,4,3,2,5,6,7,8)
print(f"Variance of data 1 {variance(data1)}")


# Co variance
import numpy as np
# example 1
x = [2.1,2.5,4.0,3.6]
y = [8,12,14,10]
z = np.stack((x,y),axis = 0)
b = np.stack((x),axis = 0)
print("Variance : ", np.var(b))
print("Co-Variance : ",np.cov(z))
print("----------------------------------------------")

# example 2:
x = [10,15,7,2,16]
y = [13,0,7,4,11]
X = np.stack((x,y), axis = 0)
print(np.cov(X))
print("------------------------------------")
# example 3:
x = np.array([[0,3,4],[1,2,4],[3,4,5]])
print("Shape of array")


# Shape Function
from numpy import array
# Example1: reshape 1D array
data = array([11, 22, 33, 44, 55])
print(data.shape)
# shape is a tuple that gives dimensions of the array.
# shape is a tuple that gives  you an indiction of the dimension in the array.
# reshape
data = data.reshape((data.shape[0],1))
print(data.shape)

#example 2: Reshape 2-D to 3-D array
from numpy import array
# list of data
data = [[11,22],[33,44],[55,66]]
# array of data
data = array(data)
print(data.shape)
# reshape
data = data.reshape((data.shape[0], data.shape[1], 1))
print(data.shape)


# Seed
import pandas as pd
import numpy as np
# setting a seed so the example is reproducible
np.random.seed(4272018)
df = pd.DataFrame(np.random.randint(low = 0, high = 20, size = (5,2)), columns = ['Commercials Watched', 'Product Purchases'])
print(df)
print(df['Commercial Watched'].var())
print(df[['Commercial Watched', 'Product Purchases']].cov())
# print(df[['Commercial Watched', 'Product Purchases']].cov())

# Question
# Read a csv file, mean , median, mode, median_high, median_low, range, var, cov and ,manually
# Read cav file data plot:
# bar plot, histogram, lineplot, scatter plot