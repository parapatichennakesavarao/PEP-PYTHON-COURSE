contact={}
while True:
    print("\n-----contact book-----")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice=(input("Enter your choice: "))

    #for adding contact
    if choice=='1':
        name=input("Enter contact name: ")
        phone=input("Enter contact phone number: ")
        contact[name]=phone
        print("Contact added successfully!")
    else:
        print("Invalid choice! Please try again.")
    #for viewing contact
    if choice=='2':
        if contact:
            print("\nContact List:")
            for name, phone in contact.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found!")
    #for searching contact
    if choice=='3':
        name=input("Enter contact name to search: ")
        if name in contact:
            print(f"Contact found: ",contact[name])
        else:
            print("Contact not found!")
    #for deleting contact
    if choice=='4':
        name=input("Enter contact name to delete: ")
        if name in contact:
            del contact[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")
    #for exiting the program
    if choice=='5':
        print("Exiting the contact book. Goodbye!")
        break


    