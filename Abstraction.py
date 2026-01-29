#What is Abstraction in Python?

#Abstraction means
#👉 hiding the internal implementation details
#👉 and showing only what is necessary to the user.

#In short:

#Abstraction = What to do, not how to do

#----Abstract_class--- is method name is present and method body is absent. who will implement the method body is child class.
"""class Payment:
    def Pay(self,amount):
        pass
class UPI(Payment):
    def Pay(self,amount):
        print("Paid Uing UPI: ",amount)
class Card(Payment):
    def Pay(self,amount):
        print("paid using card: ",amount)
u=UPI()
u.Pay(1000)
c=Card()
c.Pay(2000)"""

"""class Shape:
    def area(self):
        pass
class Circle(Shape):
    def area (self,radius):
        return 3.14*radius*radius
class Square(Shape):
    def area(self,side):
        return side*side
c=Circle()
print("Area of Circle: ",c.area(5))
s=Square()
print("Area of Square: ",s.area(4))"""

"""class Payment:
    def pay(self):
        print("Payment method not implemented")
    def pay(self,amount):
        print("Paying amount: ",amount)
class UPI(Payment):
    def pay(self,amount):
        print("Paid using UPI: ",amount)
class Card(Payment):
    def pay(self,amount):
        print("Paid using Card: ",amount)
u=UPI()
u.pay(1500)
c=Card()
c.pay(2500)
p=Payment()
p.pay(3000)"""  # This will call the base class method

#---Interface---
#An interface is a rule book that tells a class what methods it must have, but not how they work.
#An Interface is only method names(rules class) without any method body.
#The class which inherits the interface must implement all the methods of the interface.

#Example of Interface
"""class Animal:
    def speak(self):
        pass
    def walk(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")
    def walk(self):
        print("Cat walks gracefully")
d=Dog()
d.speak()
c=Cat()
c.speak()
c.walk()"""

class Course:
    def Course_info(self):
        Course_name=input("Enter Course Name: ")
        print("this is programming course",Course_name)
    def Course_duration(self):
        pass
class ExamInterface:
    def Exam_type(self):
        pass
class Python_course(Course,ExamInterface):
    
    def Course_duration(self,time):
        print("Course duration is: ",time)
    def Exam_type(self):
        print("EXAM TYPE: OFFLINE Exam")
p=Python_course()
p.Course_info()
p.Course_duration("3 months")
p.Exam_type()

