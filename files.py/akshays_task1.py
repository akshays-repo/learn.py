
#1 : Write a python program to print “Hello World!”
print("Hello World")

#2 : Write a python program to add 3 numbers with and without using user input.
print("with out int \n a = 1 \n b=2 \n c=3 ")
a,b,c = 1,2,3
print("sum of a + b + c = ",(a+b+c))
x, y, z = input("Enter a three value to add use spacebar: ").split()
print("sum of three numbers = ",int(x)+int(y)+int(z)) 

# 3 : Write a python program to find the area of a square and rectangle.
a = input( "enter the length ")
print("Area of square is ",int(a)*int(a))

#rectangle
width = input("enter the width")
height = input("enter the height")
print("Area of rectanglr is ",int(width)*int(height))

#4 : Get the characters of str from 2 to 18 using both positive and negative indexing.
Str = "This is a new beginning"
print(f'The string is {Str}')
print("postive",Str[3:20])
print("Negative",Str[-17:-3])

#listOperations():
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
print(f'The created list is {list}')
print(f'Access an item from the list using its index. list[0] :{list[0]}')
print(f'Access an item from the list using negative index. list[-4]: {list[-4]}')
list[0] = 'xyxz'
print(f'Modify an item in the list[0] : {list}')
print(f'Access the items in the list using range(slicing). list[2:]: {list[2:]}')

#setOperations():
set = { 'abcd', 786 , 2.23, 'john', 70.2 }
print(f'The created set is {set}')

#tupleOperations():
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )

print(f'The created list is {tuple}')
print(f'Access an item from the tuple using its index. tuple[0] :{tuple[0]}')
print(f'Access an item from the tuple using negative index. tuple[-4]: {tuple[-4]}') 
print(f'Modify an item in the tuple[0] : tuple is inmutable')
print(f'Access the items in the tuple using range(slicing). tuple[2:]: {tuple[2:]}')

#dictOperations():
dict = {'name': 'john','code':6734, 'dept': 'sales'}
print(f'The created Dict is {dict}')
dict["name"] = "akshays"
print(f'The modified Dict is {dict}')



    
