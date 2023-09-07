while True:
    try:
        user_input = input("Enter the original price (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break

        original_price =  int(user_input)
        percent = input("Enter the discount percentage: ")
        print(" ")

        # to get the amount to be deducted to the original price
        percentage = int(percent) / 100 * original_price
        # to get the discounted price
        discounted_price = original_price - percentage

        print(f"The original price is: ₱{original_price}. The discounted price is: ₱{discounted_price}. ")
        print(f"You saved ₱{percentage}!")
        print(" ")

    except ValueError:
        print("Invalid input. Please enter a number value for price and percentage.")
        print("")
