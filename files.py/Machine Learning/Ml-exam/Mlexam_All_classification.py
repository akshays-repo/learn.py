#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:45:53 2020

@author: akshays
"""

from sklearn.svm import SVC
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np
import pandas as pd

data= pd.read_csv('/home/akshays/programs/learn.py/files.py/Ml-exam/SalaryData_Train.csv')


#Data pre processing 
st=["workclass","education","maritalstatus","occupation","relationship","race","sex","native","Salary"]
num = preprocessing.LabelEncoder()
for i in st:
    data[i]=num.fit_transform(data[i])
data.shape

data.to_csv('/home/akshays/programs/learn.py/files.py/Ml-exam/file1.csv') 

X = data.iloc[:, :13]
Y = data.iloc[:, 13]

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=1)

#NAVIE BAYES - accuracy:  0.7838554616277142
ignb = GaussianNB()
imnb = MultinomialNB()

model_gnb = ignb.fit(X_train, y_train)
model_mnb = imnb.fit(X_train, y_train)

pred_gnb = model_gnb.predict(X_test)
pred_mnb = model_mnb.predict(X_test)


print(confusion_matrix(y_test, pred_gnb))  # GaussianNB model
print(pd.crosstab(y_test.values.flatten(), pred_gnb))  # confusion matrix using
print('accuracy: ', accuracy_score(y_test, pred_gnb))

print(confusion_matrix(y_test, pred_mnb))  # Multinomial model
print(pd.crosstab(y_test.values.flatten(), pred_mnb))  # confusion matrix using
print('accuracy: ', accuracy_score(y_test, pred_gnb))


#LOGISTIC - Accuracy:  0.8085529587270015
logistic_regression = LogisticRegression(max_iter=20000)
logistic_regression.fit(X_train, y_train)
y_pred = logistic_regression.predict(X_test)
confusion_matrix = pd.crosstab(y_test, y_pred)
print("confusion matrix: "'\n', confusion_matrix)
print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))


#SVM - Accuracy: 0.789325377092657
model_poly = SVC(kernel="rbf")
model_poly.fit(X_train, y_train)
pred_test_poly = model_poly.predict(X_test)
np.mean(pred_test_poly == y_test)

#RandomForest  - Accuracy: 0.8397149013757667
from sklearn.ensemble import RandomForestClassifier
rfiris = RandomForestClassifier(n_jobs=4,oob_score=True,n_estimators=100,criterion="entropy")

m = rfiris.fit(X_train, y_train)
preds = m.predict(X_test)

print(confusion_matrix(y_test,preds))
y = y_test.to_frame()
print('accuracy: ', accuracy_score(y,preds))

#Decison Tree - Accuracy:0.8027515332338804
from sklearn.tree import  DecisionTreeClassifier

model = DecisionTreeClassifier(criterion='entropy')
model.fit(X_train,y_train)
preds = model.predict(X_test)
confusion_matrix1 = confusion_matrix(y_test,preds)
print (confusion_matrix1)
print("Accuracy:",accuracy_score(y_test,preds))

#K nearest Neighbour  Accuracy : 0.8310956406431295, k = 49

from sklearn.neighbors import KNeighborsClassifier as KNC
acc=[]
for i in range(3,50,2):
    modelknn=KNC(n_neighbors=i)
    modelknn.fit(X_train,y_train)
    predknn=modelknn.predict(X_test)
    knnacc=np.mean(predknn==y_test)
    acc.append([knnacc,i])
acc