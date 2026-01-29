#file handling in python
#syntax file=open("data.txt","mode->r,w,a")
#Write a context in file 
"""file=open("Student.txt","w")
file.write("Name: Rahul \n")
file.write("Course: python \n")
file.close()"""
#read the file 
"""file=open("student.txt","r")
data=file.read()
print(data)
file.close()"""
# another method to read the file
"""with open("student.txt","r") as file:
    data=file.read()
    print(data)"""
#append the data in file
"""file=open("student.txt","a")
file.write("Age: 21 \n")
file.write("City: New York \n")
file.close()

#read the file after appending

file=open("student.txt","r")
data=file.read()
print(data)
file.close()"""
#readline() method
"""file=open("student.txt","r")
line1=file.readline()
line2=file.readline()
print(line1)
print(line2)
file.close()"""
#readlines() method
"""file=open("student.txt","r")
lines=file.readlines()
print(lines)
file.close()"""

