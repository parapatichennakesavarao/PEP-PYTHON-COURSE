#OOP's=to map real world entities to programming world
#four pillars of OOP's
#1.encapsulation
#2.abstraction
#3.inheritance
#4.polymorphism
#class is a blueprint of object
#object is instance of class or result of class
#constructor is special method which is automatically called when object is created
#default constructor is constructor which does not take any parameter
#parameterized constructor is constructor which takes parameters
#self is reference variable which refers to current object

#basic class and object
"""
class Student:
    print("this is Student class")
s1=Student()
print(s1)"""

#class and obbject using constructor 
#constructor
"""class Student:
    def __init__(self,Fullname):
          
        self.name=Fullname
        print("this is constructor Student class")
s1=Student("Chenna")
print(s1)"""
#parameterized constructor
"""class Student:
    def __init__(self,Fullname,rollno):
        self.name=Fullname
        self.rollno=rollno
    def display(self):
        print("Fullname: ",self.name)
        print("Rollno: ",self.rollno)
s1=Student("Chenna",20)
s2=Student("Raju",30)
s1.display()
s2.display()"""
#Car class with parameterized constructor and method
"""class Car:
    def __init__(self,brand,color):
        self.brand=brand#attribute self.color=color
        
        self.color=color
    def display_info(self):
        print("Car Information: ")
        print("brand: ",self.brand)
        
        print("color: ",self.color)
car1=Car("Toyota","Red")
car2=Car("Hyundai","Blue")
car1.display_info()
car2.display_info()
"""
#attribute is data or variable of class
#object attrubute is data or variable of object
#exapmle of object attribute is name and rollno of student which is different for different objects of class Student

#class attribute is data or variable of class which is shared by all objects of class
#exapmle of class attribute is college name which is same for all students of class Student
"""class Student:
    college_name = "Lovely Professional University"  # class attribute

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name of the student:", self.name)
        print("Marks of the student:", self.marks)
        print("College Name:", Student.college_name)
        print("--------------------")


# object creation (OUTSIDE the class)
s1 = Student("Chenna", 5)
s2 = Student("Raju", 10)
s1.display()
s2.display()
print(Student.college_name)  # Accessing class attribute directly using class name"""
#Example of class attribute and object attribute
"""class Car:
    showroom_name="Autoworld"#class Attribute
    def __init__(self,model,price):
        self.model=model#object Attribute
        self.price=price#object Attribute
    def display_info(self):
        print("Showrrom Name: ",Car.showroom_name)
        print("Car Model: ",self.model)
        print("Car Price: ",self.price)
car1=Car("Benz",1500000)
car2=Car("BMW",2000000)
car1.display_info()
car2.display_info()
print("Showroom Name Accessed Directly: ",Car.showroom_name)"""

#Example of modifying class attribute
"""class Student:
    college_name="Lovely Professional University"  # class attribute
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name of the student:",self.name)
        print("Marks of the student:",self.marks)
        print("College Name:",Student.college_name)
        print("--------------------")
# object creation (OUTSIDE the class)
s1=Student("Chenna",5)
s2=Student("Raju",10)
s1.display()
s2.display()
Student.college_name="LPU"#modifying class attribute
s1.display()
s2.display()
print(Student.college_name)  # Accessing class attribute directly using class name"""

#Example of modifying object attribute
"""class Employee:
    company_name = "TechCorp"  # class attribute

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        # if instance variable exists, it is used; else class variable
        print("Company Name:", self.company_name)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("--------------------")


# object creation
e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

# modifying salaries (object attributes)
e1.salary = 55000
e2.salary = 65000

# assigning different companies
e1.company_name = "InnoTech"     # instance attribute for e1
e2.company_name = "FutureSoft"   # instance attribute for e2

e1.display()
e2.display()"""


#Q1 total students in class when students are created class total count the number of students
"""class Class_room:
    total_students=0#class attribute
    def __init__(self,name):
        self.name=name#object attribute
        Class_room.total_students+=1#incrementing class attribute
    def display(self):
        print("Student Name: ",self.name)
        print("Total Students in Class: ",Class_room.total_students)
s1=Class_room("Chenna")

s1.display()
s2=Class_room("Raju")
s2.display()
s3=Class_room("Mohan")
s3.display()"""

#methods in class is function defined inside class or functions related to class
#instance method is method which takes self as first parameter
#static method is method which does not take self as first parameter
#class method is method which takes cls as first parameter
"""class Student:
    def __init__(self,name):
        self.name=name
    def greetings(self):
        print("Hello, my name is ",self.name)
    @staticmethod#static method
    def collage_name(name):
        print(name,"study at Lovely Professional University")
       
s1=Student("Chenna")
s1.greetings()
s1.collage_name(s1.name)"""
#Q1 create a class student object attribute name and marks
"""class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("hello",self.name,"your marks are",self.marks)
s1=Student("Chenna",85)
s1.display()"""
#same question using static method
"""class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def display(name,marks):
        print("hello",name,"your marks are",marks)
s1=Student("Chenna",90)
s1.display(s1.name,s1.marks)"""
#immutable ->int,float,string,tuple
#mutable ->list,dictionary,set

#Q2 create a class student show name as normal method  and college name as static method
"""class Student:
    def __init__(self,name):
        self.name=name
    def show_name(self):
            print("Student Name: ",self.name)
    @staticmethod
    def college_name():
        print("college name: Lovely Professional University")

s1=Student("Chenna")
s1.show_name()
s1.college_name()"""
"""class Student:
    def __init__(self,name,college_name):
        self.name=name
        self.college_name=college_name
    def show_name(self):
        print("Student Name: ",self.name)
    @staticmethod
    def collegenName(college_name):
        print("college name: ",college_name)
s1=Student("Chenna","LPU")
s1.show_name()
s1.collegenName(s1.college_name)"""

#What is Encapsulation in Python?

#Encapsulation means
#👉 wrapping data (variables) and methods (functions) into a single unit (class)
#👉 and controlling access to that data.

#In short:

#Encapsulation = Data Hiding + Controlled access

"""class Student:
    def __init__(self,name,rollno):
        self.__name=name#private variable
        self.__rollno=rollno#private variable
    def display(self):
        print("Name: ",self.__name)
        print("Rollno: ",self.__rollno)"""

#example 1
"""class Student:
    def __init__(self,marks):
        self.__marks=marks#private variable
    def get_marks(self):#getter method used to access private variable
        return self.__marks
    def set_marks(self,new_marks):#setter method used to modify private variable
        self.__marks=new_marks
s1=Student(85)
s1.set_marks(95)
print("Marks: ",s1.get_marks())"""

#example 2
"""class Bank:
    def __init__(self,balance):
        self.__balance=balance#private variable
    def get_balance(self):
        return self.__balance
    def set_balance(self,new_balance):
        self.__balance=new_balance
b1=Bank(1000)
b1.set_balance(1500)
print("Balance: ",b1.get_balance())"""

#example 3
#Bank class with deposit and withdraw methods
"""class Bank:
    def __init__(self,balance):
        self.__balance=balance#private variable
    def set_balance(self,new_balance):
        self.__balance=new_balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount>=self.__balance:
            print("Insufficient balance")
        else:
            self.__balance-=amount
    def get_balance(self):
        return self.__balance
b1=Bank(2000)
b1.set_balance(3000)
b1.deposit(500)
b1.withdraw(1000)
print("Balance: ",b1.get_balance())
"""

#What is Abstraction in Python?

#Abstraction means
#👉 hiding the internal implementation details
#👉 and showing only what is necessary to the user.

#In short:

#Abstraction = What to do, not how to do


#------inheritance------ is child class acquires properties of parent class
#Simple example of inheritance
"""class Human:
    def eat(self):
        print("eating...")
class Student(Human):
    def study(self):
        print("Studying...")
s1=Student()
s1.eat()
s1.study()"""

#Example2
"""class Animal:
    def sound(self):
        print("ANimals can speak...")
class Dog(Animal):
    def bark(self):
        print("Dog Barks...")
d1=Dog()
d1.sound()
d1.bark()"""

#EXample3
"""class Nokia:
    def feature(self):
        print("Basic Features: Calling,SMS")
class Iphone(Nokia):
    def features(self):
        print("Advanced Features: Touchscreen,Apps")
i1=Iphone()
i1.feature()
i1.features()"""

#Example4 is constructor in inheritance
"""class Parent:
    def __init__(self):
        print("This is Parent class constructor")
class Child(Parent):
    def __init__(self):
        super().__init__()#calling parent class constructor
        print("This is Child class constructor")
c1=Child()"""
#super() is used to call parent class constructor or method


#method overriding is when child class method has overrides parent class method with same name
"""class Parent:
    def show(self):
        print("This is Parent class method")
class Child(Parent):
    def show(self):
        print("This is Child class method")
c1=Child()
c1.show()#calls child class method"""

#method overriding with different parameters
"""class Parent:
    def show(self,a):
        print("This is Parent class method",a) 
class Child(Parent):
    def show(self,a,b):
        print("This is Child class method",a,b)
c1=Child()
c1.show(5,10)#calls child class method"""

#multilevel inheritance is child class inherits from multiple levels
"""class Father:
    def skills(self):
        print("Father skills: gardening ")
class Mother:
    def skills(self):
        print("Mother skills: cooking ")
class Child(Father,Mother):
    def skills(self):
        Father.skills(self)#calling Father class method
        Mother.skills(self)#calling Mother class method
        print("Child skills: programming ")
c1=Child()
c1.skills()"""

#example 
"""class Parent:
    def shape(self):
        print("This is Parent class method")
class Child(Parent):

    def shape(self):
        super().shape()#calling parent class method
        Parent.shape(self)
        print("This is Child class method")
c1=Child()
c1.shape()"""
#Q1 create a parent classes teacher and coder and child class is student inherits from both
"""class Teacher:
    def __init__(self):
        print("Teaching...")
class Coder:
    def coder(self):
        print("Coding...")
class Student(Teacher,Coder):
    def __init__(self):
        Teacher.__init__(self)
        Coder.coder(self)
        
    pass
s1=Student()"""

#Q2 create a parent class inside it make hidden variables name and rollno access it in child class
"""class Student:
    def __init__(self,name,rollno):
        self.__name=name#private variable
        self.__rollno=rollno#private variable
    def display(self):
        print("Name: ",self.__name)
        print("Rollno: ",self.__rollno)
class Child(Student):
    def show(self):
        self.display()
c1=Child("Chenna",20)
c1.show()"""

#answer 2

"""class Parent:
    def __init__(self,name,rollno):
        self.__name=name#private variable
        self.__rollno=rollno#private variable
class Child(Parent):
    def show(self):
        print("Name: ",self._Parent__name)
        print("Rollno: ",self._Parent__rollno)
c1=Child("Chenna",20)
c1.show()"""
#__x is private variable
#X is public variable
#_x is protected variable

#how to access protected variable
"""class Parent:
    def __init__(self,name,rollno):
        self._name=name#protected variable
        self._rollno=rollno#protected variable
class Child(Parent):
    def show(self):
        print("Name: ",self._name)
        print("Rollno: ",self._rollno)
c1=Child("Chenna",20)
c1.show()"""

#Q2
"""class Parent:
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
class Child(Parent):
    def show(self):
        print("Name: ",self.get_name())

c1=Child("Chenna")
c1.show()"""
#create a parent class account then it should have protected variable _balance then constructor should set the balance then method show balance should print the balance 
#create a child class savings account which inherits from account class and create a method add mooney then it should take input amount and then it should update the balance 
#finally create an object of savings account and show balance before and after adding money

"""class Account:
    def __init__(self,balance):
        
        self._balance=balance
    def show_balance(self):
        print("Balance: ",self._balance)
class SavingsAccount(Account):
    def add_money(self):
        amount=int(input("Enter amount to add: "))

        self._balance+=amount
        print("Amount added successfully")
    def withraw_money(self):
        amount=int(input("Enter the moiney to withdraw: "))
        if amount>=self._balance:
            print("Insufficient Blanace...")
        else:
            self._balance-=amount
            print("Amount Withdraw Successfully")
s1=SavingsAccount(1000)
s1.show_balance()
s1.add_money()
s1.show_balance()
s1.withraw_money()
s1.show_balance()"""

#dimentional inheritance
# is a type of inheritance where a class can inherit from multiple classes which are derived from a single parent class
class A:
    print("Class A")
class B(A):
    print("Class B")
class C(A):
    print("Class C")
        
class D(B,C):
    print("Class D")
d1=D()

#-------------------Polymorphism-----------------
#Polymorphism means "many forms", one name multiple forms.->different behaviors,->depending on the context.
#in simple words polymorphism means same function name but different behavior.  
#example of polymorphism
class Dog:
    def speak(self):
        print("Dog barks")
class Cat:
    def speak(self):
        print("Cat meows")
c1=Cat()
d1=Dog()
c1.speak()
d1.speak()






