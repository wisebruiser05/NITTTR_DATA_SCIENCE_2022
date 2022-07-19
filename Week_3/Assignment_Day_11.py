# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:23:23 2022

@author: hp
"""


# Question
# Read a csv file, mean , median, mode, median_high, median_low, range, var, cov and ,manually

import pandas as pd
import statistics as st
df = pd.read_csv('C:/Users/hp/Desktop/NITTTR_TRANING_2022/week_3/Book1.csv')
print(df)
df.drop('Name', axis = 1)
# Mean
print('\n')
print('Mean Age :',st.mean(df['Age']))
print('Mean Marks : ',st.mean(df['Marks']))
# Median
print('\n')
print('Median Age : ',st.median(df['Age']))
print('Median Marks : ',st.median(df['Marks']))
# Median_High and Median_Low
print('\n')
print('Median_High Age : ',st.median_high(df['Age']))
print('Median_Low Age : ',st.median_low(df['Age']))
print('\n')
print('Median_High Marks : ',st.median_high(df['Marks']))
print('Median_Low Marks : ',st.median_low(df['Marks']))
# Mode
print('\n')
print('Mode Age : ',st.mode(df['Age']))
print('Mode Age : ',st.mode(df['Marks']))
# Variance
print('\n')
print('Variance of Age : ',df['Age'].var())
print('Variance of Marks : ',df['Marks'].var())
print('Variance of Age and Marks : ',df[['Age','Marks']].var())
# Co-Variance
print('\n')
#print('Co-Variance of Age : ',df['Age'].cov())
#print('Co-Variance of Marks : ',df['Marks'].cov())
print('Co-Variance of Age and Marks : ',df[['Age','Marks']].cov())
# Range
# Range Age
print('\n')
Maximum_Age = max(df['Age'])
Minimum_Age = min(df['Age'])
Range_Age = Maximum_Age - Minimum_Age
print(
    f'Maximum_Age : {Maximum_Age}, Minimum_Age : {Minimum_Age}, Range_Age : {Range_Age}'
)

# Range Marks
print('\n')
Maximum_Marks = max(df['Marks'])
Minimum_Marks = min(df['Marks'])
Range_Marks = Maximum_Marks - Minimum_Marks
print(
    f'Maximum_Marks : {Maximum_Marks}, Minimum_Marks : {Minimum_Marks}, Range_Marks : {Range_Marks}'
)