import random

# Function to roll a six-sided dice
def roll_dice():
    return random.randint(1, 6)

# Function to play the dice game
def play_game(num_players, target_score):
    players_scores = [0] * num_players
    current_player = 0

    while max(players_scores) < target_score:
        input(f"{current_player + 1}'s turn (Press Enter to roll the dice)")
        dice_roll = roll_dice()
        players_scores[current_player] += dice_roll

        print(f"{current_player + 1} rolled a {dice_roll}. Total score: {players_scores[current_player]}")

        if players_scores[current_player] >= target_score:
            print(f"{current_player + 1} is the champion with a score of {players_scores[current_player]}!")
            break

        current_player = (current_player + 1) % num_players

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    target_score = int(input("Enter the target score: "))

    play_game(num_players, target_score)
