import random


# def play():
#     print("What's your pick? 'Rock', 'Paper', 'Scissor'")
#     user = input("'r' for rock, 'p' for paper, 's' for scissor: ")
#     computer = random.choice(['r', 'p', 's'])

#     if user == computer:
#         return "It's a tie"
#     # r > s, p > r, s > p

#     if is_Win(user, computer):
#         return "You won!"
#     return "You lost"

# def is_Win(player, opponent):
#     if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
#         return True


# print(play())
 
while True:
    # User's choice
    user_choice = input(
        "Enter your choice (Rock, Paper, Scissors) or 'q' to quit: ").lower()

    if user_choice == 'q':
        break  # Exit the game if the user enters 'q'

    # Computer's choice
    choices = ['r', 'p', 's']
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice in choices:
        print(f"Computer chose {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")

# Game over
print("Thanks for playing!")
