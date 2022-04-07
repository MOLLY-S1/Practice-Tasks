""" Component 2 (How much) V2
Use try/accept and pull error messages out of the loop"""

error = "please enter a whole number between 1 and 10\n"
valid = False

# Continue asking until a valid amount is entered
while not valid:
     try:
     # Ask for amount
          user_balance = int(input("How much would you like to play with $"))

     #check if amount is too low
          if 0 < user_balance <= 10:
               print(f"you are playing with ${user_balance}")
               valid = True
          else:
               print(error)

     except ValueError:
          print(error)
