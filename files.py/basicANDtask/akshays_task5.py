#TASK-5
#1 Write a Python class to reverse a string word by word.
class ParentClass:
    
    def __init__(self, userinput):
        self.userinput = userinput
        
    def reverseWord(self):
        reverse = reversed(userinput)
        string = " "
        return string.join(reverse) 
        
userinput = input("enter the string: ").split(" ")

obj = ParentClass(userinput)
print(obj.reverseWord())
        

#2 Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.
class GetAndPrint:
    def __init__(self):
        self.input = ""
    def getInput(self):
        userinput = input("enter the input: ")
        self.input = userinput
    def printInput(self):
        print(f'user input is : {self.input}')

obj2 = GetAndPrint()
obj2.getInput()
obj2.printInput()        

#3 Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def areaOfcircle(self):
        area = math.pi * (self.radius ** 2)
        print(f'The area is : {area}')
    def perimeterOfcircle(self):
        perimeter =2 * math.pi * self.radius
        print(f'The perimeter of circle is : {perimeter}')

radius = int(input("enter the radius: "))
obj3 = Circle(radius)
obj3.areaOfcircle()
obj3.perimeterOfcircle()

#4 Create a Student class and initialize it with name and roll number. Make methods to :
class Student:
    def __init__(self, name , rollnumber):
        self.name = name
        self.rollnumber = rollnumber
    def setAge(self):
        age = int(input("enter the age of the student: "))
        self.age = age
    def setMark(self):
        mark = int(input("enter the mark of the student: "))
        self.mark = mark
    def displayDetails(self):
        print(f' \n name : {self.name} \n')
        print(f'age : {self.age} \n')
        print(f'rollnumber : {self.rollnumber} \n')
        print(f'mark : {self.mark}')
    
name = input('enter the name of the student: ')
rollnumber = int(input("enter the roll number: "))

obj4 = Student(name, rollnumber)
obj4.setAge()
obj4.setMark()
obj4.displayDetails()        

#5 Create a Time class and initialize it with hours and minutes.
class Time():

  def __init__(self, hours, mins):
    self.hours = hours
    self.mins = mins

  def addTime(t1, t2):
    t3 = Time(0,0)
    if t1.mins+t2.mins > 60:
      t3.hours = (t1.mins+t2.mins)//60
    t3.hours = t3.hours+t1.hours+t2.hours
    t3.mins = (t1.mins + t2.mins) % 60
    return t3

  def displayTime(self):
    print (f'Time is {self.hours} hours and {self.mins} minutes.')

  def displayMinute(self):
    print ((self.hours*60)+self.mins)

a = Time(1,60)
b = Time(5,40)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()