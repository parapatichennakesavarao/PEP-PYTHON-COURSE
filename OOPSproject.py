class BankAccount:
    def __init__(self,account_number,account_name,balance):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=balance
    def deposite(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient Balance"
    def get_balance(self):
        return self.balance
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        
        interest = self.balance * 0.04
        return interest
    
class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return 0
    
class BankAPP:
    def __init__(self):
        self.account=None
    def create_account(self,account_type,account_number,account_name,balance):
        if account_type=="savings":
            self.account=SavingsAccount(account_number,account_name,balance)
        else:
            self.account=CurrentAccount(account_number,account_name,balance)
        return "Account Created Successfully"
    def deposite_amount(self,amount):
        return self.account.deposite(amount)
    def withdraw_amount(self,amount):
        return self.account.withdraw(amount)
    def check_balance(self):
        return self.account.get_balance()
    def get_interest(self):
        return self.account.calculate_interest()
app=BankAPP()
print(app.create_account("savings","123456","Chenna",1000))
print("Enter the Deposite amount: ", app.deposite_amount(500))
print("Enter the Withdraw amount: ", app.withdraw_amount(200))
print("Current Balance: ", app.check_balance())
print("Interest: ", app.get_interest())