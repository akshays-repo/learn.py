# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 19:52:02 2020

@author: user
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt

sal=pd.read_csv("/home/akshays/Desktop/learn.py/files.py/Logistic regression/salary1.csv")
sal

X = sal[['age', 'workclass','education','educationno','maritalstatus','occupation','relationship','race','sex','capitalgain','capitalloss','hoursperweek']]
y = sal['Salary']  
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2) 

logistic_regression= LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)

print ("test dataset: ",X_test) 
print ("predicted value: ",y_pred) 
confusion_matrix = pd.crosstab(y_test, y_pred)
print("confusion matrix: "'\n',confusion_matrix)

sn.heatmap(confusion_matrix, annot=True)


print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))
plt.show()
sal.to_csv("salary1.csv",index=False)


