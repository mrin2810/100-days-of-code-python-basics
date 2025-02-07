import random
letters = [chr(i) for i in range(65, 91)]
letters.extend([chr(i) for i in range(97, 123)])

numbers = [chr(i) for i in range(48, 58)]

special = [chr(i) for i in range(32, 47)]

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters?\n"))
nr_symbols = int(input("How many symbols?\n"))
nr_numbers = int(input("How many numbers?\n"))

password = ""
# Easy
for i in range(nr_letters):
  password += letters[random.randint(0, len(letters) - 1)]

for i in range(nr_symbols):
  password += special[random.randint(0, len(special) - 1)]

for i in range(nr_numbers):
  password += numbers[random.randint(0, len(numbers) - 1)]
