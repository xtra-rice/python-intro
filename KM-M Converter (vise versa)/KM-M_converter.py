#kilometer converter to miles
def km_converter():
    try: 
        user_miles = input("Enter kilometer: ")
        value = float(user_miles)
        km_formula = value / 1.609
        print(f"{value} kilometers is equivalent to {km_formula:.2f} miles.\n")
    except ValueError: 
        print("Invalid Input. Please enter a number.\n")
        

def m_converter():
    try: 
        user_miles = input("Enter miles: ")
        value = float(user_miles)
        m_formula = value * 1.609
        print(f"{value} miles is equivalent to {m_formula:.2f} kilometers.\n")
    except ValueError: 
        print("Invalid Input. Please enter a number.\n")
        
            
while True:
    user_input = input("1. Kilometers to miles. / 2. miles to kilometers: / 3. Exit: ")
    if user_input == "1":
        km_converter()
    elif user_input == "2":
        m_converter()
    elif user_input.lower() == "3":
        print("Exiting program. \n")
        break
    else:
        print("Please choose between 1, 2 and 3.\n")














