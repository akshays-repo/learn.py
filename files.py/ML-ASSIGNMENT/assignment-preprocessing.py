#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:37:56 2020

@author: akshays
"""

import numpy as np
import pandas as pd

data = pd.read_csv('/home/akshays/Desktop/learn.py/files.py/ML-ASSIGNMENT/SalaryData_Test.csv')
col = ['workclass','education','maritalstatus','occupation','relationship','race','sex','native','Salary']

#Encoding
from sklearn import preprocessing
encoder = preprocessing.LabelEncoder()
for i in col:
    data[i]=encoder.fit_transform(data[i])
data.shape

#MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
for j in col:
    mm=MinMaxScaler()
    data[col]=mm.fit_transform(data[col])
data[col]

#normalising
def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)

df_norm = norm_func(data.iloc[:,:])
df_norm.to_csv('df_norm.csv')

