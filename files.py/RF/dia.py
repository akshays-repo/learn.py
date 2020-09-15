#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:29:02 2020

@author: akshays
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:44:57 2020

@author: user
"""
import pandas as pd
import numpy as np

df = pd.read_csv("/home/akshays/Desktop/learn.py/files.py/naivebayes/Diabetes_RF.csv")
x = df.iloc[:,:7]
y = df.iloc[:,7]

from sklearn.model_selection import train_test_split
Xtrain,Xtest,ytrain,ytest = train_test_split(x,y,test_size=0.3, random_state=0)

from sklearn.ensemble import RandomForestClassifier
rfiris = RandomForestClassifier(n_jobs=4,oob_score=True,n_estimators=100,criterion="entropy")

m = rfiris.fit(Xtrain, ytrain)
preds = m.predict(Xtest)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
print(confusion_matrix(ytest,preds))
print('accuracy: ', accuracy_score(ytest,preds))

