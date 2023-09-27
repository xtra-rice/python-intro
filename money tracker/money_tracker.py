# missing features: view expenses list

print("$", "-" * 28, "$")
print("|   Welcome to Money Tracker   |")
print("$", "-" * 28, "$")
balance = 0

def deposit(current_balance):
    amount = float(input("Enter the deposit amount: "))
    if amount > 0:
        new_balance = current_balance + amount
        print(f"Deposited: ${amount}. New balance: ${new_balance} \n")
        return new_balance, amount
    else:
        print("Invalid amount for deposit. Please enter a positive amount.")


def check_balance():
    return balance


def withdraw():
    print(f"Balance: {balance}")
    withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
    if withdrawal_amount >= balance:
        print("Insufficient funds. Withdraw cancelled")
    else:
        total = balance - withdrawal_amount
        print(f"Withdrew: ${withdrawal_amount}. New balance: ${total} \n")
        return total


def expenses():
    item = input("Where did your money go? ")
    item_amount = float(input("Enter amount: "))
    print(f"Your expense is {item} with an amount of ${item_amount}")
    with open("expenses.txt", "w") as f:
        f.write(f"{item}: ${item_amount}\n")
    return item_amount


while True:
    choice = input(
        "Enter choice ('deposit', 'withdraw', 'check balance', 'expenses', 'quit'):").lower()
    if choice == 'deposit':
        # deposit_amount = deposit()
        balance, deposit_amount = deposit(balance)
    elif choice == "check balance":
        balance_check = check_balance()
        print(f"Current balance: ${balance_check}\n")
    elif choice == "withdraw":
        withdraw_money = withdraw()
    elif choice == 'expenses':
        expense_amount = expenses()
        balance -= expense_amount
        print(f"New balance: ${balance}\n")
    elif choice == 'quit':
        quit()
    else:
        print("Invalid input. Try again.\n")
