import pandas as pd
import numpy as np

data = pd.read_csv('/home/akshays/Desktop/learn.py/files.py/preprocessing/SalaryData_Train.csv')
print(data)

from sklearn import preprocessing
st = ["workclass", "education", "maritalstatus", "occupation", "relationship", "race", "sex", "native","Salary"]
num = preprocessing.LabelEncoder()
for i in st:
    data[i]=num.fit_transform(data[i])
data.shape

from sklearn.preprocessing import MinMaxScaler
#df = ["age",	"workclass",	"education",	"educationno",	"maritalstatus",	"occupation",	"relationship",	"race",	"sex",	"capitalgain",	"capitalloss",	"hoursperweek",	"native	Salary"]
st = ["workclass", "education", "maritalstatus", "occupation", "relationship", "race", "sex", "native","Salary"]
for j in st:
    mm=MinMaxScaler()
    data[st]=mm.fit_transform(data[st])
data[st]
def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)

df_norm = norm_func(data.iloc[:,:])
df_norm
