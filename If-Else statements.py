password = "billbobben123"
access = False

if pwd == "billbobben123":
  access = True
else:
  access = False

# note that this is not how most systems handle passwords

# elif is short for else if

num = 5
studentsAnswer = int(input("Guess the number_"))

if num == 5:
  print("You got it!")
elif num == 4 or 6:
  print("You were 1 away from the answer!")
else:
  print("You wrong.")
