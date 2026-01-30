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


class Human:
    @staticmethod
    def speak():
        print("Human speaks")
    
class Robot:
    @staticmethod
    def speak():
        print("Robot beeps")
class Alien:
    @staticmethod
    def speak():
        print("Alien communicates telepathically")
def speak():
    print("This is a generic speak function")
h=Human()
r=Robot()
a=Alien()
h.speak()
r.speak()
a.speak()
speak()

#create a class with a method role()
#create 2 class student and teacher 
#Student will print(I am a student) 
#Teacher will print(I am a teacher)
#create another class assistant that inherits both student and teacher

#1.create and object of assisstant
#2.call role()
#3. observe which method is called 
class Person:
    def role(self):
        print("I am a generic role")
class Student(Person):
    def role(self):
        print("I am a student")
class Teacher(Person):
    def role(self):
        print("I am a teacher")
class Assistant(Student,Teacher):
    pass
a=Assistant()
a.role()
