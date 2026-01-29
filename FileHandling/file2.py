"""file=open("data.txt","w")#write mode
file.write("Name: Alice \n")#writing data to file
file.write("Course: Data Science \n")#writing data to file
file.close()#closing the file
file=open("data.txt","a")#append mode
file.write("Age: 25 \n")#writing data to file
file.write("City: San Francisco \n")#writing data to file
file.close()#closing the file
file=open("data.txt","r")#read mode
data=file.read()
words=data.split()
print(len(words))   #printing number of words in the file
file.close()"""
#counting occurrence of a word in a file
file=open("data.txt","r")
data=file.read()
print(data)
count=data.lower().count("data")
print("word Count: ",count)  # Output: 2
file.close()

file=open("data.txt","r")
data=file.read()
print("reversed data: ")
reversed_data=data[::-1]
print(reversed_data)  # Output: .ocsicnarF naS :ytiC
file.close()

file=open("data.txt","r")
data=file.read()
print(data)
data=data.replace("Alice", "kalyan babu")
print("after replacing name: ")
print(data)