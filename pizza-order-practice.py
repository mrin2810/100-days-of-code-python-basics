print("Welcome to Python Pizza Deliveries!")
size = input("Choose Size: S/M/L: ")
pepperoni = input("Pepperoni: Y/N: ")
extra_cheese = input("Extra Cheese: Y/N: ")

total = 0
if size == "S":
  total += 15
elif size == "M":
  total += 20
elif size == "L":
  total += 25
else:
  print("You typed the wrong input")

if pepperoni == "Y":
  if size == "S":
    total += 2
  else:
    total += 3

if extra_cheese == "Y":
  total += 1

print("Your final bill is: $" + str(bill) + ".")
