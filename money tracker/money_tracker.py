print("$", "-" * 28, "$")
print("|   Welcome to Money Tracker   |")
print("$", "-" * 28, "$")
balance = 0


def deposit():
    global balance
    try:
        amount = float(input("Enter the deposit amount: "))
        if amount > 0:
            balance += amount
            print(f"Deposited: ₱{amount:.2f} New balance: ₱{balance:.2f} \n")
        else:
            print("Invalid amount for deposit. Please enter a positive amount.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number for the deposit amount.\n")

def check_balance():
    global balance
    print(f"Current balance: ₱{balance:.2f}\n")


def withdraw():
    global balance
    try:
        print(f"Balance: ₱{balance:.2f}")
        withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
        if withdrawal_amount >= balance:
            print("Insufficient funds. Withdraw canceled\n")
        else:
            balance -= withdrawal_amount
            print(f"Withdrew: ₱{withdrawal_amount:.2f}. New balance: ₱{balance:.2f} \n")
    except ValueError:
        print("Invalid input. Please enter a valid number for the deposit amount.\n")


def display_expenses():
    with open("expenses.txt", "r", encoding="utf-8") as f:
        expenses_lines = f.readlines()
        if not expenses_lines:
            print("No expenses recorded yet\n")
        else:
            print("List of expenses")
            for index, line in enumerate(expenses_lines, start=1):
                print(f"{index}. {line.strip()}")


def expenses():
    global balance
    item = input("Where did your money go? ")
    item_amount = float(input("Enter amount: "))
    print(f"Your expense is {item} with an amount of ₱{item_amount:.2f}")
    with open("expenses.txt", "a", encoding="utf-8") as f:
        f.write(f"{item}: ₱{item_amount:.2f}\n")
    balance -= item_amount 
    print(f"New balance: ₱{balance}\n")


while True:
    choice = input(
        "Enter choice: 1.deposit, 2.withdraw, 3.check balance, 4.expenses, 5.display expenses, 6.quit: ").lower()
    if choice == '1':
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        check_balance()
    elif choice == '4':
        expenses()
    elif choice == '5':
        display_expenses()
    elif choice == '6':
        quit()
    else:
        print("Invalid input. Try again.\n")


# print("$", "-" * 28, "$")
# print("|   Welcome to Money Tracker   |")
# print("$", "-" * 28, "$")
# balance = 0

# def deposit(current_balance):
#     amount = float(input("Enter the deposit amount: "))
#     if amount > 0:
#         new_balance = current_balance + amount
#         print(f"Deposited: ${amount}. New balance: ${new_balance} \n")
#         return amount, new_balance
#     else:
#         print("Invalid amount for deposit. Please enter a positive amount.")

# def check_balance(current_balance):
#     print(f"Current balance: {current_balance}")
#     return current_balance


# def withdraw(current_balance):
#     print(f"Balance: {current_balance}")
#     withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
#     if withdrawal_amount >= current_balance:
#         print("Insufficient funds. Withdraw cancelled")
#         return current_balance
#     else:
#         total = current_balance - withdrawal_amount
#         print(f"Withdrew: ${withdrawal_amount}. New balance: ${total} \n")
#         return total

# def display_expenses():
#     with open("expenses.txt", "r") as f:  # Open the file in "read" mode
#         expenses_lines = f.readlines()
#         for line in expenses_lines:
#             print(line.strip() + ",")  # Print each line without leading/trailing

# def expenses(current_balance):
#     item = input("Where did your money go? ")
#     item_amount = float(input("Enter amount: "))
#     print(f"Your expense is {item} with an amount of ${item_amount}")
#     with open("expenses.txt", "a") as f:
#         f.write(f"{item}: ${item_amount}\n")
#     new_balance = current_balance - item_amount
#     return new_balance


# while True:
#     choice = input(
#         "Enter choice 'deposit', 'withdraw', 'check balance', 'expenses', 'display expenses', 'quit': ").lower()
#     if choice == 'deposit':
#         balance, deposit_amount = deposit(balance)
#     elif choice == "check balance":
#         balance = check_balance(balance)
#     elif choice == "withdraw":
#         balance = withdraw(balance)
#     elif choice == 'expenses':
#         balance = expenses(balance)
#     elif choice == 'display expenses':
#         display_expenses()
#     elif choice == 'quit':
#         quit()
#     else:
#         print("Invalid input. Try again.\n")

