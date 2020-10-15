# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 13:32:57 2020

@author: user
"""

import pandas as pd
import numpy as np
iris=pd.read_csv("/home/akshays/Desktop/learn.py/files.py/knn/iris.csv")

#importing train test split and subsplit it 
from sklearn.model_selection import train_test_split
train,test=train_test_split(iris,test_size=0.2)
trainx=train.iloc[:,0:4]
trainy=train.iloc[:,4]
testx=test.iloc[:,0:4]
testy=test.iloc[:,4]


#importing model
from sklearn.neighbors import KNeighborsClassifier as KNC

#for k=3
modelknn3=KNC(n_neighbors=3)
modelknn3.fit(trainx,trainy)
predknn3=modelknn3.predict(testx)
knnacc3=np.mean(predknn3==testy)


#for k=5
modelknn5=KNC(n_neighbors=5)
modelknn5.fit(trainx,trainy)
predknn5=modelknn5.predict(testx)
knnacc5=np.mean(predknn5==testy)

#we have to repeat these steps with some k values for finding better accuracy model.finally choose k value which gives high accuracy.we can find k value by putting codes in a for loop.
acc=[]
for i in range(3,50,2):
    modelknn=KNC(n_neighbors=i)
    modelknn.fit(trainx,trainy)
    predknn=modelknn.predict(testx)
    knnacc=np.mean(predknn==testy)
    acc.append([knnacc,i])

 