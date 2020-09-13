import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


################################# Iris Data Set ################################


df = pd.read_csv('iris.csv')
x = df.iloc[:,:4]
y = df.iloc[:,4]

Xtrain,Xtest,ytrain,ytest = train_test_split(x,y,test_size=0.3, random_state=0)

ignb = GaussianNB()
imnb = MultinomialNB()

model_gnb = ignb.fit(Xtrain,ytrain)
model_mnb = imnb.fit(Xtrain,ytrain)

pred_gnb = model_gnb.predict(Xtest)
pred_mnb = model_mnb.predict(Xtest)

print(confusion_matrix(ytest,pred_gnb)) # GaussianNB model
print(pd.crosstab(ytest.values.flatten(),pred_gnb)) # confusion matrix using 
print('accuracy: ',accuracy_score(ytest, pred_gnb))

print(confusion_matrix(ytest,pred_mnb)) # Multinomial model
print(pd.crosstab(ytest.values.flatten(),pred_mnb)) # confusion matrix using 
print('accuracy: ',accuracy_score(ytest, pred_gnb))



########################## Reading the Diabetes Data ###########################


Diabetes = pd.read_csv("Diabetes_RF.csv")
colnames = list(Diabetes.columns)
predictors = Diabetes.iloc[:,:8]
target = Diabetes.iloc[:,8]

X_train,X_test,y_train,y_test = train_test_split(predictors,target,test_size=0.3, random_state=0)

Dgnb = GaussianNB()
Dmnb = MultinomialNB()

model_Dgnb = Dgnb.fit(X_train,y_train)
model_Dmnb = Dmnb.fit(X_train,y_train)

pred_Dgnb = model_Dgnb.predict(X_test)
pred_Dmnb = model_Dmnb.predict(X_test)

print(confusion_matrix(y_test,pred_Dgnb))
print(pd.crosstab(y_test.values.flatten(),pred_Dgnb))
print('accuracy: ',np.mean(pred_Dgnb==y_test))

print(confusion_matrix(y_test,pred_Dmnb))
print(pd.crosstab(y_test.values.flatten(),pred_Dmnb))
print("Accuracy: ",np.mean(pred_Dmnb==y_test))

