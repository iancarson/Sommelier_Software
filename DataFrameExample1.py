# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:26:18 2021

@author: jdk450
"""

import os

import matplotlib
import numpy as np
import pandas as pd
#For data visulaization: 
#https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
#import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
os.getcwd()

#os.chdir('Python\Data') #change to the directory where the data is located if necessary

# read dataset from CSV fileimport pandas
data = pd.read_csv('brain_size.csv', sep=';', na_values=".")

#take a look at the data
data

#get dimensions of data frame, it should be 40x8
data.shape

#Generate descriptive statistics.
data.describe()

#It has columns
data.columns
#columns can be addressed by name
print(data['Weight'])

#get the mean value FSIQ for females
data[data['Gender'] == 'Female']['FSIQ'].mean()

#get the mean value FSIQ for males
data[data['Gender'] == 'Male']['FSIQ'].mean()

#groupby: splitting  a dataframe on values of categorical variables - this should give the
# same values that we obtained from the two previous steps
groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['FSIQ']:
    print ((gender, value.mean()))
    
#get mean, count and median values of other features for each gender
groupby_gender.mean()
print groupby_gender.count()
groupby_gender.median()
#Get the MRI mean for both genders.
var = data['MRI_Count'].mean
    
# Box plots of different columns for each gender
groupby_gender = data.groupby('Gender')
groupby_gender.boxplot(column=['FSIQ', 'VIQ', 'PIQ'])

#pandas.plotting.scatter_matrix( ) enables you to draw a matrix of scatter plots
#https://pandas.pydata.org/docs/reference/api/pandas.plotting.scatter_matrix.html
# Scatter matrices for different columns
pd.plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])
pd.plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']])

