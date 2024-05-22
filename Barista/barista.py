#AUTOMATED BARISTA
''' list of question in SB:
    Order
    Size
    Name
    Payment (Cash or Card)
'''
menu = ["Iced Caramel Machiatto", "Java Chip", "Seasalt Caramel", "Iced Caffe Latte"]
prices = [300, 310, 280, 320]
size = ["Tall", "Grande", "Venti"]

def cashier():
    while True: 
        try: 
            cashier = input("\nWelcome to Stubucks! May I take your order? (y/n): ").lower()
            if cashier not in ("y", "n"):
                raise ValueError("Enter only (y/n)")
            if cashier == "y":
                customer = int(input(f"\nHere's our menu. {menu} Ente your choice (1, 2, 3, or 4): ").upper()) - 1
                if 0 <= customer <len(menu):
                    order = menu[customer].split()[0]
                    drink_price = prices[customer]
                    sizes()
                    name = input("\nMay I know your name?: ")
                    payment(drink_price)
                    print(f"\nHere's your order {name}! Have a nice day, thank you!")
                    break
                else: 
                    print("Invalid choice. Please enter a number between 1 and 4. ")
            elif cashier == "n":
                break
        except ValueError as e:
            print(f"Error: {e}")
           
def payment(drink_price):
    payment_method = input("\nCash or Card?: ").lower()
    if payment_method == "cash":
        while True:
            amount = input("\nAmount of Cash: ")
            try: 
                amount = int(amount)
                change = amount - drink_price
                if change >= 0: #sufficient payment
                    print(f"\nI received ₱{amount}")
                    if change > 0:
                        print(f"Your change is ₱{change}.")
                    break
                else:
                    print(f"Insufficient money. Please pay a larger bill, your total is ₱{drink_price}")
            except ValueError:
                print("Invalid input. Please enter a numerical amount.")
    elif payment_method.lower() == "card":
        print("Payment Successful. Thank you!")
    
def sizes():
    while True:
        try:
            cs_size = int(input(f"\nWhat size? {size} Enter your choice (1, 2, or 3): ").upper()) - 1
            if 0 <= cs_size <len(size):
                order = size[cs_size]
                print(f"\nYou chose: {order}")
                break
            else:
                print(f"Please choose between {size}")
        except ValueError as e:
            print(f"Error: Enter your choice (1, 2, or 3)")

            
cashier()
