import numpy as np
 
#first method
arr = np.array([1,2,3,4,5,6,7,8])
x= [False,True,False,True,False,True,False,True]
even = arr[x]
print(even)

#second method
even_cont = []
for i in arr:
    if i%2 == 0:
        even_cont.append(True)
    else:
        even_cont.append(False)
print(even_cont)

even1 = arr[even_cont]
print(even1)