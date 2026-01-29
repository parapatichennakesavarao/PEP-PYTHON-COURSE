#Creating and manipulating a text file in Python
file=open("person.txt","w")#write mode 
file.write("Name: chenna \n")#writing data to file
file.write("city: srikakulam \n")#writing data to file
file.close()#closing the file
file=open("person.txt","a")#append mode
file.write("age: 22 \n")#writing data to file
file.write("course: java \n")#writing data to file
file.close()#closing the file
file=open("person.txt","r")#read mode
file=file.readlines()
print(file)
file=open("person.txt","r")
line1=file.readline()#reading first line
line2=file.readline()#reading second line
print(line1)
print(line2.upper())
file.close()
file=open("person.txt","r")
data=file.read()
print(len(data))#printing length of data
file.close()




