# importing required libraries
import pandas as pd
from sklearn.cluster import KMeans


# read the train and test dataset
train_data = pd.read_csv('/home/akshays/Desktop/learn.py/files.py/K MEAN/train-data.csv')
print(train_data)
test_data = pd.read_csv('/home/akshays/Desktop/learn.py/files.py/K MEAN/test-data.csv')
print(test_data)

# shape of the dataset
print('Shape of training data :',train_data.shape)
print('Shape of testing data :',test_data.shape)

# Now, we need to divide the training data into differernt clusters
# and predict in which cluster a particular data point belongs.  


model = KMeans()  

# fit the model with the training data
model.fit(train_data)

# Number of Clusters
print('\nDefault number of Clusters : ',model.n_clusters)

# predict the clusters on the train dataset
predict_train = model.predict(train_data)
print('\nCLusters on train data',predict_train) 

# predict the target on the test dataset
predict_test = model.predict(test_data)
print('Clusters on test data',predict_test) 

# Now, we will train a model with n_cluster = 3
model_n3 = KMeans(n_clusters=3)

# fit the model with the training data
model_n3.fit(train_data)

# Number of Clusters
print('\nNumber of Clusters : ',model_n3.n_clusters)

# predict the clusters on the train dataset
predict_train_3 = model_n3.predict(train_data)
print('\nCLusters on train data',predict_train_3) 

# predict the target on the test dataset
predict_test_3 = model_n3.predict(test_data)
print('Clusters on test data',predict_test_3)
