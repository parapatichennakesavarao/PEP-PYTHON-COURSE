students_info={}
while True:
    print("\n-----Student Details-----")
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Exit")
    choice=input("Enter your Choice: ")
    #for adding student
    if(choice=='1'):
        name=input("Enter Student Name: ")
        roll_number=int(input("Enter the Roll Number: "))
        reg_no=int(input("Enter the Registration Number: "))
        location =input("Enter the location: ")
        students_info[roll_number]={'Name':name, 'Registration Number':reg_no, 'Location':location}
        print("Student Details Added Successfully!")
    else:
        print("Invalid Choice ! plaese try again.")
    #for viewing students
    if(choice=='2'):
        if students_info:
            print("\nStudent List: ")
            for roll_number, details in students_info.items():
                print(f"Roll Number: {roll_number}, Details: {details}")
        else:
            print("No student details found!")
    #for searching student
    if(choice=='3'):
        roll_number=int(input("Enter Roll Number to search: "))
        if roll_number in students_info:
            print(f"Student found: ",students_info[roll_number])
        else:
            print("Student not found!")
    #for deleting student
    if(choice=='4'):
        roll_number=int(input("Enter Roll Number to delete: "))
        if roll_number in students_info:
            del students_info[roll_number]
            print("Student details deleted successfully!")
        else:
            print("Student not found!")
    
    #for exiting the program
    if(choice=='5'):
        print("Exiting the Student Details. Goodbye!")
        break
