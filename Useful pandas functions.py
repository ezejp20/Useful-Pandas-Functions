# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 09:59:45 2020

@author: I519797
"""
# Import pandas and seaborn
import pandas as pd
import seaborn as sns
import numpy as np
#Load the mpg dataset
mpg = sns.load_dataset('mpg')

#%% Info method: gives info about the dataset: The information is the total number of the data, how many columns are, the columns name with how many data are not Null and the data type, as well as the memory usage.

mpg.info()

#%% Describe:  get all the numerical data basic statistics; which is the Count, Mean, STD (Standard Deviation), Minimum, 25% Quantile, 50% Quantile (Median), 75% Quantile, and Maximum.

mpg.describe()

#%%#Input exclude parameter as 'number' to exclude all the numerical columns
#information includes Count, Unique (Number of the Unique Value), Top (The most Frequent Value), and Freq (Frequency of the Top value).
mpg.describe(exclude = 'number')

#%% The agg function aggregates many statistics into one series/dataframe object 

mpg.agg('mean')
mpg.agg(['mean', 'std'])
#we could also use function here, e.g. Numpy
#mpg.agg(np.mean)

#%% corr function returns the correlation of the numerical values 

mpg.corr()

#%% Group By function 

mpg_groupby_origin = mpg.groupby('origin')
#Groupby object have many method similar to the series or dataframe; for example .mean
mpg_groupby_origin.mean()
# .T is a method to transpose the DataFrame
mpg_groupby_origin.agg(['mean', 'std']).T