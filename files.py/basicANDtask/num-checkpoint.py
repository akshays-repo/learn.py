import numpy

import numpy as np

#check version
print(np.__version__)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(type(arr)) # prints the type of array

print(arr.shape) # prints the number of elements in the array
print(arr[0], arr[1]) # prints the elements in the index position

arr[0] = 5 # changes an element of array arr
print(arr)

#####################Dimensions in Arrays#########################

#0-D arrays
import numpy as np
arr = np.array(40)
print(arr)


#1-D array
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)


#2-D arrays
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


#3-D arrays
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)


#check number of dimensions
#NumPy Arrays provides the ndim attribute that returns an integer
#that tells us how many dimensions the array have.
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


#higher dimensional arrays
#An array can have any number of dimensions. When the array is created,
#you can define the number of dimensions by using the ndmin argument.
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)


#access array elements
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])


#get 3rd and 4th elements
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])


#access 2-D arrays
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arr[0, 1])


#access 3-D arrays
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])


