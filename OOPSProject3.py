
"""Create a Library Management System where different library items calculate borrowing charges differently.
Library item (parent class)
Book and magazie (child class)
LibraryApp(main class)

Book IS-A libraryitem
Magazine IS-A libraryitem
LibraryApp HAS-A libraryitem

Output format
Item Type: Book
Borrow Days: 5
Borrowing Charge: 50
Or 
Item Type: Magazine
Borrow Days: 3
Borrowing Charge: 30"""

class LibraryItem:
    def __init__(self,title,item_id):
        self.title=title
        self.item_id=item_id
    def Calculate_Charges(self):#interface method
        pass
class Book(LibraryItem):#child class
    def Calculate_Charges(self,days):#polymorphic method
        
        total_charge=days * 10
        return total_charge
class Magazine(LibraryItem):#child class
    def Calculate_Charges(self,days):#polymorphic method
        
        total_charge=days * 5
        return total_charge

class LibraryApp:#main class
    def __init__(self):
        self.item=None#HAS-A relationship 
    def add_item(self,item_type,title,item_id):#method to add item
        if item_type=="book":#creating Book object
            self.item=Book(title,item_id) 
        else:
            self.item=Magazine(title,item_id)#creating Magazine object 
        return "Item added successfully"
    def get_borrowing_charge(self,days):#calling polymorphic method 
        return self.item.Calculate_Charges(days)#returning total charge 
app=LibraryApp()
print(app.add_item("book","Python Programming","B001"))
print("Borrowing Charge for Book:",app.get_borrowing_charge(5))
print(app.add_item("magazine","Tech Today","M001"))
print("Borrowing Charge for Magazine:",app.get_borrowing_charge(3))






        