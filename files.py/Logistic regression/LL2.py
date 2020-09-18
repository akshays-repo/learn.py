
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
logistic_regression= LogisticRegression(max_iter=2000)
""" solver='liblinear' , saga """

logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)


confusion_matrix = pd.crosstab(y_test, y_pred)
print("confusion matrix: "'\n',confusion_matrix)

sn.heatmap(confusion_matrix, annot=False)

print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))

X_test.head()
y_pred

sal.to_csv("salary1.csv",index=False)


