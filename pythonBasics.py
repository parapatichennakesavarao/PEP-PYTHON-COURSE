"""a=21,22,23
b=6.1,6.2
c="chenna"
d=b<a
print(a)
print(b)
print(c)
print(d)

x=int(input("Enter the Number: "))
if(x>=18):
    print("you are eligible to this")
else:
    print("you are not")
y=int(input("Enter the value: "))
if(y%2==0):
    print("even")
else:
    print("not even")

marks=int(input("Enter the marks: "))
if(marks>=90):
    print("Grade A")
elif(marks>=75):
    print("Grade B")
elif(marks>=50):
    print("Grade C")
else:
    print("Grade D")


signal=input("Enter the signal color: ")
if(signal=="red"):
    print("stop")
elif(signal=="yellow"):
    print("get ready")
elif(signal=="Green"):
    print("go")

for i in range(0,12):
    print(2*i)
#print odd numbers
for i in range(1,15):
    if(i%2!=0):
        print(i)
#to print the pattern
x=int(input("Enter the number: "))
for i in range(1,6):
    print("*"*i)
#to print multiplication table
x=int(input("Enter the number: "))
for i in range(1,11):
    print(x,"*",i,"=",x*i)

from operator import add

#function to add two numbers
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
def add(a,b):
    return a+b
print("The sum is:",add(a,b))

#lambda function(without defining a function)
add=lambda a,b: a+b
print("The sum is:",add(a,b))

x=int(input("Enter the number: "))
y=int(input("Enter the number: "))
add=lambda x,y:x+y
print("The sum is:",add(x,y))"""

"""#Q1
a=1
b=1.3
c="hello"
d=a<b
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Q2
x="15000"
y=int(x)
bonus=5000
print("Total salary is:",y+bonus)

#Q3
hot=int(input("Enter the temperature: "))
if(hot>=30):
    print("It's a hot day")
elif(hot>=15):
    print("It's a cold day")
else:
    print("It's a lovely day")

#Q4
tabel=int(input("Enter the number: "))
for i in range(1,11):
    print(i,")",tabel,"*",i,"=",tabel*i)
#Q5
reversed=int(input("Enter the number: "))
i=0
while(reversed>0):
    digit=reversed%10
    i=i*10+digit
    reversed=reversed//10
print("Reversed number is:",i)

#Q6
num=int(input("Enter the number: "))
def even_odd(n):
    if(n%2==0):
        return "Even"
    else:
        return "Odd"
print(even_odd(num))

#Q7
cube=lambda x:x**3
num=int(input("Enter the number: "))
print("The cube of the number is:",cube(num))

#List Operations
marks=[10,20,30,40]
marks.append(100)
marks.insert(2,50)#insert 50 at index 2
marks.insert(1,75)#insert 75 at index 1
marks.remove(30)#remove 30 from the list
marks.pop()#remove last element in list 
marks.sort()#sort the list in ascending order
marks.reverse()#reverse the list
print(marks)
print(max(marks))"""

numbers=[5,10,15,20,25,30,35,40,45,50]
numbers.append(55)
numbers.insert(2,7)
print(numbers[::-1])

print(numbers)
