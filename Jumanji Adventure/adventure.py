name = input("Type your name: ")
print(f"Welcome, {name}, to the Jumanji Adventure Game!")

def play():
    print("\nYou find yourself in a dense, ancient jungle after rolling the dice. The sound of wild animals and rustling leaves surrounds you. You spot a path ahead. What do you want to do?")

    while True:
        user = input("1. Follow the path deeper into the jungle\n2. Climb a nearby tree to get a better view\n3. Shout for help\n").lower()

        if user in ["1", "follow"]:
            print("\nAs you venture deeper into the jungle, you come across a rushing river with a rickety bridge. It looks unstable. What will you do?")
            while True:
                answer = input("1. Cross the bridge cautiously.\n2. Look for an alternative route along the riverbank.\n3. Turn back and explore another path in the jungle.\n").lower()

                if answer in ["1", "cross"]:
                    print("\nYou carefully make your way across the rickety bridge. Just as you reach the other side, you hear a loud creak, and the bridge collapses behind you. You're relieved to have made it across safely. As you continue down the path, you discover a hidden treasure chest partially buried in the dirt.")
                    while True:
                        user = input("\nDo you want to:\n1. Open the treasure chest.\n2. Ignore the treasure and keep moving forward.\n").lower()
                        
                        if user in ["1", "open"]:
                            print("\nYou can't resist the temptation and decide to open the treasure chest. Inside, you find a sparkling gemstone and a map that seems to lead to an exit from Jumanji! You feel like you've hit the jackpot.")
                            print("\nCongratulations, you've successfully completed the Jumanji adventure!")
                            return

                        elif user in ["2", "ignore"]:
                            print("\nYou decide to ignore the treasure and keep moving forward, continuing your adventure in the world of Jumanji.")
                            return

                        else:
                            print("Invalid input. Please choose a valid option (1 or 2).")

                elif answer in ["2", "look"]:
                    print("\nYou climb the tree and get a bird's-eye view of the jungle. In the distance, you spot a group of adventurers who look lost.")
                    while True:
                        user = input("\nDo you want to:\n1. Yell and wave to get their attention?\n2. Stay hidden and observe them for a while?\n3. Climb down and rejoin the path on the ground?\n").lower()

                        if user in ["1", "yell"]:
                            print("\nYou call out to the group of adventurers and wave your arms. They spot you and approach cautiously. It turns out they are also trapped in Jumanji and are relieved to find a fellow traveler.")
                            print("\nTogether, you decide to join forces and explore deeper into the jungle. After a long and arduous journey, you discover the hidden Jumanji shrine, which can transport you back to the real world.")
                            print("\nCongratulations, you've successfully completed the Jumanji adventure!")
                            return

                        elif user in ["2", "stay"]:
                            print("\nYou choose to stay hidden and observe the group of adventurers for a while. They eventually move on, and you continue your solo journey through the jungle.")
                            return
                        
                        elif user in ["3", "climb"]:
                            print("\nYou decide to climb down from the tree and rejoin the path on the ground, continuing your adventure in the world of Jumanji.")
                            return

                        else:
                            print("Invalid input. Please choose a valid option (1, 2, or 3).")

                elif answer in ["3", "turn"]:
                    print("\nYou decide to turn back and explore another path in the jungle, hoping to discover new adventures and challenges.")
                    break  # Go back to the main menu

                else:
                    print("Invalid input. Please choose a valid option (1, 2, or 3).")

        elif user in ["2", "climb"]:
            print("\nYou climb a nearby tree to get a better view. In the distance, you spot a group of adventurers who look lost.")
            while True:
                user = input("\nDo you want to:\n1. Yell and wave to get their attention?\n2. Stay hidden and observe them for a while?\n3. Climb down and rejoin the path on the ground?\n").lower()

                if user in ["1", "yell"]:
                    print("\nYou call out to the group of adventurers and wave your arms. They spot you and approach cautiously. It turns out they are also trapped in Jumanji and are relieved to find a fellow traveler.")
                    print("\nTogether, you decide to join forces and explore deeper into the jungle. After a long and arduous journey, you discover the hidden Jumanji shrine, which can transport you back to the real world.")
                    print("\nCongratulations, you've successfully completed the Jumanji adventure!")
                    return

                elif user in ["2", "stay"]:
                    print("\nYou choose to stay hidden and observe the group of adventurers for a while. They eventually move on, and you continue your solo journey through the jungle.")
                    return
                
                elif user in ["3", "climb"]:
                    print("\nYou decide to climb down from the tree and rejoin the path on the ground, continuing your adventure in the world of Jumanji.")
                    return

                else:
                    print("Invalid input. Please choose a valid option (1, 2, or 3).")

        elif user in ["3", "shout"]:
            print("\nYou shout for help, but your voice only echoes through the dense jungle. Suddenly, a mischievous monkey appears and steals one of your belongings!")
            while True:
                user = input("\nDo you want to:\n1. Chase the monkey to retrieve your item?\n2. Let the monkey go and continue exploring the jungle?\n3. Turn back and explore another path in the jungle?\n").lower()

                if user in ["1", "chase"]:
                    print("\nYou decide to chase the monkey to retrieve your stolen item. It leads you deeper into the jungle, and after a thrilling chase, you manage to recover your belonging.")
                    print("\nYou continue your adventure through the jungle, determined to conquer Jumanji's challenges.")
                    return

                elif user in ["2", "let"]:
                    print("\nYou decide to let the mischievous monkey go and continue your journey through the jungle, keeping an eye out for further surprises and adventures.")
                    return

                elif user in ["3", "turn"]:
                    print("\nYou choose to turn back and explore another path in the jungle, hoping to discover new adventures and challenges.")
                    break  # Go back to the main menu

                else:
                    print("Invalid input. Please choose a valid option (1, 2, or 3).")

play()