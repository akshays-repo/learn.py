import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("/home/akshays/programs/learn.py/files.py/decisiontree/salary1.csv")
print(data)
data.head()
print(data['Salary'].unique())
print(data.Salary.value_counts())

from sklearn.model_selection import train_test_split
x=data.iloc[:,:13]
y=data.iloc[:,13]
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

