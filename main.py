import random as ra

# emoji: rock, paper, scissors
player_one = ["\U0001F91C", "\U0001FAF1", "\U0000270C"]
player_two = ["\U0001F91B", "\U0001FAF2", "\U0000270C"]

player_choce = int(input("What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors.\t"))

if player_choce < 0 or player_choce >3:
    print("Wrong number, please try again")
else:
    computer_choce = ra.randint(0, 2)


    print(f"Your chose: {player_one[player_choce]}  VS {player_two[computer_choce]}  :Computer choce")

    if (player_choce == 0 and computer_choce == 2) or (player_choce == 1 and computer_choce == 0) or (player_choce == 2 and computer_choce == 1):
        print("You Win!")
    elif player_choce == computer_choce:
        print("Draw!")
    else:
        print("You Lose!")