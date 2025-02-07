import random

graphics = [
  """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
  """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
  """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
print("You Chose:")
print(graphics[player_choice])

computer_choice = random.randint(0, 2)
print("Computer Chose:")
print(graphics[computer_choice])

if player_choice == computer_choice:
  print("It's a Tie")

elif (player_choice + 1) % 3 == computer_choice:
  print("You Loose")
else:
  print("You Win")
