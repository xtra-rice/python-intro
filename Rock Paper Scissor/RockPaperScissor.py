import random

options = (["r", "p", "s"])
user_score = 0
computer_score = 0
print("Welcome to ROCK, PAPER, SCISSOR!")

while True:
    user = input("Choose your pick 'r', 'p', 's' or 'q' to quit. ").lower()
    if user == 'q':
        break
    print()

    if user not in options:
        print("Invalid Input. Try again.")
    else:
        computer = random.choice(options)

        if computer == user:
            print("It's a tie")
        elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
            print("You win!")
            user_score += 1
        else:
            print("Computer win!")
            computer_score += 1

    if (user_score == 5):
        print("Congratulations! You got first 5 points")
        break

    elif (computer_score == 5):
        print("Sorry, the computer beat you to 5 points")
        break

print("Thanks for playing!")
