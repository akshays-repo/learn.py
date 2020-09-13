#Take 3 int values from user  and print the greatest number among them.

a,b,c = input("enter 3 numbers . use spacebar ").split()
print(f'Three numbers are {a} {b} {c}')
if a > b and a > c:print(f'The greatest number is {a}')
elif b > a and b > c:print(f'The greatest number is {b}')
else:
    print(f'The greates number is {c}')



#Check whether a number is even or not.

number = input("Enter the number")
if (int(number) % 2) == 0:print(f'Given number {number} is even number')
else:
    print(f'Given number {number} is not a even number')



# Check whether a number is positive, negative or zero.  
number = input("Enter the number")
if int(number) > 0:print(f'Given number {number} is even postive')
if int(number) < 0:print(f'Given number {number} is even negative')
else:
     print(f'Given number {number} is even zero')



#Take values of length and breadth of a rectangle from user and check if it is square or not.
length = input("Enter the length")
breadth = input("enter the breadth")
if int(length) == int(breadth):print("it is a SQUARE")
else:
    print("Not a square")



#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.
name = input("please enter employee name")
yearOfService = input("please enter year of service")
salary = input(f'please enter salary of {name}')
if (int(yearOfService) > 5):
    new_salary = (21*int(salary))/20
    print(f'You got a Hike{name} new salary is {new_salary}')
else:
    print(f'sorry {name} you are not eligible for hike')



#A school has following rules for grading system:
mark = input("Enter the Mark")

if(int(mark) > 80):print("The grade is A")
elif(int(mark)>60 and int(mark)<=80):print("The grade is B")
elif(int(mark)>50 and int(mark)<=60):print("The grade is C") 
elif(int(mark)>45 and int(mark)<=50):print("The grade is D") 
elif(int(mark)>25 and int(mark)<=45):print("The grade is E") 
else:
    print("The grade is F")



#A student will not be allowed to sit in exam if his/her attendence is less than 75%. Take following input from user:
numberOfclasses = input("Enter the number of classes")
numberOfclassAttend = input("Enter the number of classes attended")
attendPercentage = (int(numberOfclassAttend)/int(numberOfclasses))*100
if (int(attendPercentage) < 75):
    print(f'percentage of class attended is  {attendPercentage} and student is not allowed to sit in exam ')
else:
     print(f'percentage of class attended is  {attendPercentage} and student is  allowed to sit in exam ')



#Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
numberOfclasses = input("Enter the number of classes")
numberOfclassAttend = input("Enter the number of classes attended")
attendPercentage = (int(numberOfclassAttend)/int(numberOfclasses))*100
if (int(attendPercentage) < 75):
    n = input("Did you submit medical cetificate (Y/N)")
    if( n == 'Y'):
            print(f'percentage of class attended is  {attendPercentage} and student is  allowed to sit in exam ')
    else:
            print(f'percentage of class attended is  {attendPercentage} and student is not allowed to sit in exam ')
            
else:print(f'percentage of class attended is  {attendPercentage} and student is  allowed to sit in exam ')


