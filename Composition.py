#---Composition---

#Composition: don't relay on inheritance, instead use objects of other classes to achieve the desired functionality.

#Example of Composition
"""class Address:
    def __init__(self,city):
        self.city=city
    def show_address(self):#method to show address
        print("City:",self.city)
class Student:
    def __init__(self,name,city):
        self.name=name
        self.address=Address(city)  #composition  #creating Address class object inside Student class
    def show_student(self):
        print("Name:",self.name)
        self.address.show_address() #using Address class method
s=Student("Abhiram","Washington DC")
s.show_student()"""

#create a class engine then create a class car has A engine 
class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self,model):
        self.model=model
        self.engine=Engine() #composition
    def start_car(self):
        print("Car model:",self.model)
        self.engine.start() #using Engine class method
c=Car("Toyota")
c.start_car()