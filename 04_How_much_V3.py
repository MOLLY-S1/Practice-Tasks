""" Component 2 (How much) V3
Makes the code more efficient - includes the valid range as a basis for while loops
"""

error = "That was not a valid input\n"
user_balance = 0

# Continue asking until a valid amount is entered
while not 1 <= user_balance <= 10:
     try:
     # Ask for amount
          user_balance = int(input("Please enter a whole number between 1 and 10\n"
                                   "How much would you like to play with $"))
          print()

     except ValueError:
          print(error)

print(f"You are playing with ${user_balance}")

