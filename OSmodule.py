import os
current_path=os.getcwd()# Get the current working directory
print("Current Working Directory:",current_path)
item=os.listdir(current_path)# List all files and directories in the current directory
print("List of files and directories in '",current_path,"':",item)

myfolder="TestFolder"# Name of the new directory to be created
if not os.path.exists(myfolder):# Check if the directory already exists
    os.mkdir(myfolder)# Create a new directory
    print("Directory",myfolder,"created")
else:
    print("Directory",myfolder,"already exists")

file_name="sample.txt"# Name of the new file to be created
file_path=os.path.exists(file_name)
print("Does the file",file_name,"exist?",file_path)
