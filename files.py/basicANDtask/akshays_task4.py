#Write a Python program to reverse a string.
string = input("enter the string")
reverseString = string[::-1] 
print ("the reversed string is :",reverseString)
    
#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
number=int(input("Input a number to compute the factiorial : "))
print("factoral of a number is :",factorial(number))

#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def calculateLowerAndUpper(string):
    upperCase = 0;
    lowerCase = 0;
    for i in range(len(string)):
        if string[i].islower():
            lowerCase += 1
        else:
            upperCase += 1
    print(f'Total Upper cases are {upperCase}')
    print(f'Total lower cases are {lowerCase}')
    
sring = input("enter the string : ")
calculateLowerAndUpper(sring)


#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
userInput = input("enter the words :").split('-')
userInput.sort()
print('sorted list is ','-'.join(userInput))

#Write a Python program to square and cube every number in a given list of integers using Lambda.
list1 = [1,2,3,4,5,6,7,8]
square = map(lambda x: x ** 2, list1)
cube = map(lambda x: x ** 3, list1)
 
print(list(square))
print(list(cube)) 

#Write a Python program to find if a given string starts with a given character using Lambda.
userString = input("Enter the string ")
userChar = input("Enter the char ")

check = lambda x, y: True if x.startswith(y) else False

print (check(userString, userChar))


 





    