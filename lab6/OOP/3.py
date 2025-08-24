class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  
        self.__balance = balance                
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance = {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance = {self.__balance}")
        else:
            print("Insufficient balance or invalid amount!")

    def get_account_details(self):
        return f"Account Number: {self.__account_number}, Balance: {self.__balance}"

account1 = BankAccount("123456789", 1000)

print(account1.get_account_details())   
account1.deposit(500)                   
account1.withdraw(200)                  
account1.withdraw(2000)
print(account1.get_account_details())   