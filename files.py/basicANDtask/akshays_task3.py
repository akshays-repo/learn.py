#Print a multiplication table.
number = input("enter the number to print multply table")
for i in range(1,11):
    mult = int(number) * int(i)
    print(f'{number} * {i} = {mult}')


#You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
list1 = [1,2,3,4,5,6,7,8]
list2=[]
for i in list1:
    l2 = int(i) * int(i)
    list2.append(l2)
print(f'new list is :{list2}')



#Using range (1,101), make two list, one containing all even numbers and other containing all odd numbers.
even=[]
odd = []
for i in range(1,101):
    if (int(i)%2 == 0):even.append(i)
    else:odd.append(i)
print(f'even list is {even} \n')
print(f'odd list is {odd} \n')

#From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
newlist = even + odd
newlist2 = []
    
for num in newlist:
    if (num % 4 == 0 or num % 6 == 0 or num % 8 == 0 or num % 10 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 9 == 0):
        newlist2.append(num)
print(f'final output : {newlist2}')



#From a list containing ints, strings and floats, make three lists to store them separately.
list1 = [12, 23,43,54,34,2,4,5,'hi','hello','how','are','you',1.2,43.3,53,4.53,55.5,464.6,43.4]
list_int = []
list_string = []
list_float = []
for i in list1:
    if isinstance(i , int):
        list_int.append(i)
    elif isinstance(i , str):
        list_string.append(i)
    elif isinstance(i , float):
        list_float.append(i)

print(f'the parent list is {list1} \n')
print(f'the int list is {list_int} \n')
print(f'the string list is {list_string} \n')
print(f'the float list is {list_float} \n')

    


#Using range (1,101), make a list containing only numbers which are divisible by 3.
list1 = []
for i in range(1,101):
    if (int(i) % 3 == 0):
        list1.append(i)
    print(f'the is list is {list1}')



#Check whether a number is Armstrong or not.
num = int(input("Enter a number: "))  
sum = 0  
temp = num  
        
while temp > 0:  
    digit = temp % 10  
    sum += digit ** 3  
    temp //= 10  
        
if num == sum:  
    print(num,"is an Armstrong number")  
else:  
    print(num,"is not an Armstrong number")  

#Write a program to print a number given by user but digits reversed.
Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print(f" Reverse of entered number is = {Reverse}" ) 

#Check whether a string is palindrome or not.
Number = int(input("Please Enter any Number: "))    
Temp = Number
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
if (Reverse == Temp):
    print("Palindrome")
else:
    print("Not a Palindrome")    

#Remove punctuations from a string.
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!;;;;, what said is  this ---and  went. to otty"
nopunctuations = ""

for char in my_str:
    if char not in punctuations:
        nopunctuations = nopunctuations + char
print(my_str ,'\n')
print(nopunctuations)

#Find the max and min value in a dictionary.
my_dict = {'x':500, 'y':5874, 'z': 560}
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])


#Write a program to find the sum of n natural numbers.

number = int(input("enter the number"))
sum = number*(number+1)/2
print(f'the sum is {sum}')

#Write a program to find the factors of a number. 
number = int(input("enter the number"))
print("factors are")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)
