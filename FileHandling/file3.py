"""file=open("movies.txt","w")
file.write("1st Movie: Inception \n")
file.write("2nd Movie: Interstellar \n")
file.write("3rd Movie: OG \n")
file.close()
file=open("movies.txt","r")
data=file.read()
print(data[0:10])  # Output: 1st Movie: Inception
file.close()
file=open("movies.txt","r")
data=file.read()
words=data.split()
for word in words:#reversing each word in the file
    print(word[::-1])  # Output: :eiM ts1 noitpecnI :dn2 rellretsnI :dr3 GO
file.close()"""
try:
    file=open("movies.txt","r")
    print(file.read())
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    print("Execution completed.")
    file.close()
