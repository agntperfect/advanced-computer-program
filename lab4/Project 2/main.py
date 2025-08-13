import os
from datetime import datetime

CUSTOMERS_FILE = "customers.txt"
TRANSACTIONS_FILE = "transactions.txt"

def load_customers():
    customers = {}
    if os.path.exists(CUSTOMERS_FILE):
        with open(CUSTOMERS_FILE, "r") as f:
            for line in f:
                try:
                    name, acc_num, balance = line.strip().split(",")
                    customers[acc_num] = {"name": name, "balance": float(balance)}
                except ValueError:
                    continue
    return customers

def save_customers(customers):
    with open(CUSTOMERS_FILE, "w") as f:
        for acc_num, data in customers.items():
            f.write(f"{data['name']},{acc_num},{data['balance']}\n")

def log_transaction(acc_num, transaction_type, amount):
    with open(TRANSACTIONS_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp},{acc_num},{transaction_type},{amount}\n")

def add_customer(name, acc_num, initial_balance):
    customers = load_customers()
    if acc_num in customers:
        raise ValueError("Account number already exists.")
    if initial_balance < 0:
        raise ValueError("Initial balance cannot be negative.")

    customers[acc_num] = {"name": name, "balance": initial_balance}
    save_customers(customers)
    print(f"Customer {name} added successfully with account number {acc_num}.")

def deposit(acc_num, amount):
    customers = load_customers()
    if acc_num not in customers:
        raise ValueError("Account number not found.")
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")
    
    customers[acc_num]["balance"] += amount
    save_customers(customers)
    log_transaction(acc_num, "DEPOSIT", amount)
    print(f"Deposit successful! New balance: {customers[acc_num]['balance']:.2f}")

def withdraw(acc_num, amount):
    customers = load_customers()
    if acc_num not in customers:
        raise ValueError("Account number not found.")
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    if customers[acc_num]["balance"] < amount:
        raise ValueError("Insufficient funds.")
    
    customers[acc_num]["balance"] -= amount
    save_customers(customers)
    log_transaction(acc_num, "WITHDRAWAL", amount)
    print(f"Withdrawal successful! New balance: {customers[acc_num]['balance']:.2f}")

if __name__ == "__main__":
    if not os.path.exists(CUSTOMERS_FILE):
        with open(CUSTOMERS_FILE, "w") as f:
            f.write("Ram,1001,5000\n")
            f.write("Shyam,1002,3000\n")
            f.write("Hari,1003,1000\n")

    try:
        add_customer("Abhishek", "1004", 20000)
        deposit("1001", 500)
        withdraw("1002", 1500)
        withdraw("1003", 2000)
    except Exception as e:
        print("Error:", e)