#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:54:15 2020

@author: akshays
"""
import pandas as pd
data = pd.read_csv("/home/akshays/Desktop/learn.py/files.py/RF/iris.csv")
print(data)
print(data)
print(data['Species'].unique())
print(data.Species.value_counts())

from sklearn.model_selection import train_test_split
x=data.iloc[:,:4]
y=data.iloc[:,4]
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size = 0.2,random_state=0)

from sklearn.tree import  DecisionTreeClassifier

model = DecisionTreeClassifier(criterion='entropy')
model.fit(train_x,train_y)
preds = model.predict(test_x)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
confusion_matrix1 = confusion_matrix(test_y,preds)
print (confusion_matrix1)
print("Accuracy:",accuracy_score(test_y,preds))
