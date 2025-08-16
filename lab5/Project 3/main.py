class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"रु {amount:.2f} deposited successfully.")
            print(f"New balance: रु{self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"रु {amount:.2f} withdrawn successfully.")
                print(f"New balance: रु {self.balance:.2f}")
            else:
                print("Insufficient funds! Cannot withdraw more than current balance.")
        else:
            print("Withdrawal amount must be positive.")
    
    def show_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: रु {self.balance:.2f}")
        print("-" * 40)

account = BankAccount("Islam Mohammad", "ACC001", 1000.00)
print("Initial Account Information:")
account.show_balance()
print("Performing deposit of रु 500:")
account.deposit(500.00)
print()
print("Balance after deposit:")
account.show_balance()
print("Performing withdrawal of रु 200:")
account.withdraw(200.00)
print()
print("Final balance:")
account.show_balance()
print("Demonstrating error handling:")
print("\n1. Trying to withdraw more than balance:")
account.withdraw(2000.00)
print("\n2. Trying to deposit negative amount:")
account.deposit(-100.00)
print("\n3. Trying to withdraw negative amount:")
account.withdraw(-50.00)