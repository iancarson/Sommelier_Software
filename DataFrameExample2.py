# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:54:28 2019

@author: jdk450
"""
import os
import numpy as np
import pandas as pd
import matplotlib as mtpl
mtpl.use('TkAgg')
os.getcwd()

# read dataset from CSV file
df_fraud= pd.read_csv('payment_fraud.csv')

#look at the first five samples and last five samples
df_fraud.head()
df_fraud.tail()

#get summary statistics of this data
df_fraud.describe()

#get the number of samples and features
df_fraud.shape

#look at the payment method column
df_fraud['paymentMethod']
#slice rows
df_fraud [0:4]
df_fraud [4:8]
df_fraud.loc[0:3]

#select by features
df_fraud.loc[:, ['accountAgeDays', 'paymentMethod']]

#select a specific row and features
df_fraud.loc[1, ['accountAgeDays', 'paymentMethod']]

#Select via the position of the passed integers
df_fraud.loc[0]
df_fraud.loc[4]
df_fraud.iloc[4]

#select specific value
df_fraud.at[1, 'paymentMethod']
df_fraud.iloc[4,3]

#integer slicing
df_fraud.iloc[5:8, 0:3]

df_fraud.iloc[5:8, 4:]
df_fraud.iloc[:, 5:]
y = df_fraud.iloc[:, 5:]
y

df_fraud.iloc[[1, 5, 8], [0, 3]]
df_fraud.iloc[[1, 5, 8], [1, 4]]

df_fraud.iloc[2:6, :]
df_fraud.iloc[:, 2:5]

#Using a single column’s values to select data.
df_fraud[df_fraud.paymentMethod=='creditcard']
df_fraud[df_fraud.accountAgeDays> 500]
#Using the Paypal column values to select data
var = df_fraud[df_fraud.paymentMethod=='paypal', df_fraud.label== 1]

#fraudulent transactions only
df_fraud[df_fraud.label ==1]

#mean for numeric values
df_fraud.mean()

#cumumulative sum
ts=df_fraud.apply(np.cumsum)

ts.plot()

