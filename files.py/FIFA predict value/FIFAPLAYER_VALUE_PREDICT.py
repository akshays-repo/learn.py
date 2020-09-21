#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 21:19:21 2020

@author: akshays
"""

import numpy as np
import pandas as pd

df = pd.read_csv('/home/akshays/Desktop/learn.py/files.py/FIFA predict value/data.csv')
df.count()
data = df[['Age','Overall','International Reputation','Position','Height','Weight','Skill Moves','Crossing','Finishing','HeadingAccuracy','ShortPassing','Volleys','Dribbling','Curve','FKAccuracy','LongPassing','BallControl','Acceleration','SprintSpeed','Agility','Reactions','Balance','ShotPower','Jumping','Stamina','Strength','LongShots','Aggression','Interceptions','Positioning','Penalties','Vision','Value']]
        

from sklearn import preprocessing
encoder = preprocessing.LabelEncoder()
#data["Club"]=encoder.fit_transform(data["Club"].astype(str))
data["Position"]=encoder.fit_transform(data["Position"].astype(str))
data["Weight"]=encoder.fit_transform(data["Weight"].astype(str))
data["Value"]=encoder.fit_transform(data["Value"].astype(str))
data["Height"]=encoder.fit_transform(data["Height"].astype(str))

new_data = data.dropna(axis = 0, how ='any')  
new_data.isna().sum()
X = new_data.iloc[:,:7]
Y = new_data.iloc[:,7]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

#NAVIE BAYES - highest accuracy
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

ignb = GaussianNB()
imnb = MultinomialNB()

model_gnb = ignb.fit(X_train,y_train)
model_mnb = imnb.fit(X_train,y_train)

pred_gnb = model_gnb.predict(X_test)
pred_mnb = model_mnb.predict(X_test)


print(confusion_matrix(y_test,pred_gnb)) # GaussianNB model
print(pd.crosstab(y_test.values.flatten(),pred_gnb)) # confusion matrix using 
print('accuracy: ',accuracy_score(y_test, pred_gnb))

print(confusion_matrix(y_test,pred_mnb)) # Multinomial model
print(pd.crosstab(y_test.values.flatten(),pred_mnb)) # confusion matrix using 
print('accuracy: ',accuracy_score(y_test, pred_gnb))


#LOGISTIC
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
logistic_regression= LogisticRegression(max_iter=20000)
""" solver='liblinear' , saga """
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)
confusion_matrix = pd.crosstab(y_test, y_pred)
print("confusion matrix: "'\n',confusion_matrix)
print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))

#SVM
from sklearn.svm import SVC
model_poly = SVC(kernel = "rbf")
model_poly.fit(X_train,y_train)
pred_test_poly = model_poly.predict(X_test)
np.mean(pred_test_poly==y_test)
