import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))

computer_choice = random.randin(0, 2)

if player_choice == computer_choice:
  print("It's a Tie")

elif (player_choice + 1) % 3 == computer_choice:
  print("You Loose")
else:
  print("You Win")
