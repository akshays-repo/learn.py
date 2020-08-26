#final task -AKSHAY - S

# 1.Write a Python program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
import pandas as pd
data1 = pd.Series([1,2,3,4,5,6,7,8,9])
print(data1)



# 2. Write a Python program to convert a dictionary to a Pandas series.
import pandas as pd
orginal_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
orginal_dict_to_pandas = pd.Series(orginal_dict)
print(orginal_dict_to_pandas)



# 3.Write a Python program to change the data type of given a column or a Series. 
import pandas as pd 
data3 = pd.Series([100, 200, 'python', 300.12, 400])
print('orginal data :\n',data3)
#data3 = data3.astype(float,  errors='ignore')
data3 = pd.to_numeric(data3, errors='coerce')
print('\n new data :\n',data3)



# 4.Write a Pandas program to change the order of index of a given series.
import pandas as pd
data4 = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
print("Original Data Series:")
print(data4)
data4 = data4.reindex(index = ['B','A','C','D','E'])
print("Data Series after changing the order of index:")
print(data4)



#5 Write a Pandas program to create the mean and standard deviation of the data of a given Series.
import pandas as pd
data5 = pd.Series([1,2,3,4,5])
print('means is :',data5.mean())
print('std is :',data5.std())



#6 Write a Pandas program to convert year-month string to dates adding a specified day of the month.
#this method is without using date parse 
import pandas as pd
data6 = pd.Series(['Jan 2011', 'Feb 2012', 'Mar 2013'])
date = 3
def convert(month):
    if(month == 'Jan'):
        return '01'
    elif(month == 'Feb'):
        return '02'
    elif(month == 'Mar'):
        return '03'
new_item = []
for items in data6.iteritems():
    dateandyear = items[1].split(' ') #get the date and year 
    month = dateandyear[0] #get the month 
    year = dateandyear[1] #get the year
    convmonth = convert(month) #convert the month
    result = str(date) + '-' +str(convmonth) + '-' +str(year)
    print(result)    
    new_item.append(result)
print(new_item)

finaloutput = pd.Series(new_item)
print('before the process', data6)
print("after the process", finaloutput)



#7 Write a Pandas program to stack two given series vertically and horizontally
import pandas as pd
series1 = pd.Series(range(7))
series2 = pd.Series(list('akshays'))
print("Original Series:")
print(series1)
print(series2)
series1.append(series2)
result = pd.concat([series1, series2], axis=1)
print(result)


    
#8 Write a Pandas program to join the two given dataframes along rows and assign all data.
import pandas as pd
data1 = pd.DataFrame({
        'rank': ['1', '2', '3'],
         'name': ['jhon cena', 'under taker', 'michal jackson'], 
        'wins': [20, 30, 90]})
data2 = pd.DataFrame({
        'rank': ['4', '5', '6'],
        'name': ['Mark jump', 'West type', 'Don arun'], 
        'wins': [91, 50, 18]})

print("Original DataFrames:")
print(data1)
print(data2)
print('\n')
result_data = pd.concat([data1,data2])
print(result_data)



#9 Write a Pandas program to find and replace the missing values in a given DataFrame which do not have any valuable information.
import pandas as pd
import numpy as np
data1 = pd.DataFrame({
        'rank': ['1', '3',np.nan],
         'name': ['jhon cena', 'under taker', 'michal jackson'], 
        'wins': [20, np.nan, 90]})
print (data1)
print('\n')
result = data1.fillna(0)
print(result)



#10 Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group. Using the following dataset find the mean, min, and max values of purchase amount (purch_amt) group by customer id (customer_id).
import pandas as pd
data = pd.DataFrame({
'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
print("\n")
print(data)
result = data.groupby('customer_id').agg({'purch_amt': ['mean', 'min', 'max']})
print('\n')
print(result)


#11 Write a Pandas program to split the following dataframe into groups and count unique values of 'value' column. Go to the editor
import pandas as pd 
data = pd.DataFrame({'id': [1,1,2,3,3,4,4,4], 
                  'value': ['a','a','b','none','a','a','none','a'] }) 
iid = data['id'].value_counts()   
value = data['value'].value_counts() 
print('total id :\n:', iid)
print('total value :\n',value)


#12 Write a NumPy program to convert an array to a float type.
import numpy as np
arr =  np.array([1,23,4,5,5,6,6])
conv_arr = arr.astype(float)
print(f'old array {arr} \n')
print(f'new array {conv_arr} \n')

#13 Write a NumPy program to divide each row by a vector element.
import numpy as np
arr= np.array([[1,2,3,4],[1,4,5,6],[12,23,43,45]])
vector = np.array([3,21,3])
output = (arr / vector[:,None])
print(output)

#14 Write a NumPy program to access last two columns of a multidimensional columns.
import numpy as np
arr= np.array([[1,2,3,4],[1,4,5,6],[12,23,43,45]])
print(f'the array is \n {arr} \n')
print(f'the last two column is \n {arr[:,[2,3]]}')

#15 Write a NumPy program to stack 1-D arrays as row wise.
import numpy as np
arr= np.array([[1,2,3,4],[1,4,5,6],[12,23,43,45]])
vector = np.array([3,21,3,4])
new_array =  np.row_stack((arr, vector))
print(f'the new array is \n {new_array}')

#16 Write a NumPy program to extract all the elements of the first row and second row from a (4x4) array.
import numpy as np
arr= np.array([[1,2,3,4],[1,4,5,6],[12,23,43,45],[21,23,43,43]])
newarray = arr[[0,],[1,]]
print(newarray)


#17 Write a NumPy program to generate six random integers between 10 and 30.
import numpy as np
arr = np.random.randint(10,30,6)
print(arr)

#18 Write a NumPy program to sort a given array of shape 2 along the first axis, last axis and on flattened array.
import numpy as np
arr = np.array([[10,40],[30,20]])
print("array:")
print(arr)
print("first axis:")
print(np.sort(arr, axis=0))
print("last axis:")
print(np.sort(arr))
print("flattened array:")
print(np.sort(arr ,axis=None))


#19 Write a NumPy program to create a structured array from given student name, height, class and their data types. Now sort by class, then height if class are equal.
import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
students = [('akshay', 3, 8.5), ('raman', 4 ,2.5),('ashik', 7, 2.0), ('rahul', 9, 1.1)]
students = np.array(students, dtype=data_type)   
print("array:")
print(students)
print("height")
print(np.sort(students, order='height'))    


#20 Write a NumPy program to sort the student id with increasing height of the students from given students id and height. Print the integer indices that describes the sort order by multiple columns and the sorted data.
import numpy as np
student_id = np.array([1, 2, 3, 4, 5, 6, 7])
student_height = np.array([4., 2., 5., 1., 8., 4., 49])
result = np.lexsort((student_id, student_height))
print("Sorted result:")
print(result)
print("Sorted data:")
for n in result:
  print(student_id[n], student_height[n])