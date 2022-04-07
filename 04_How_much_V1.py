""" Component 2 (How much)
Ask user how much they want and check it is a valid integer between 1 and 10.
If it is then this amount will become the balance on their account.
"""

user_balance = int(input("how much do you want to play with? : "))
# Ask until valid amount is entered
while not 1 <= user_balance <= 10:
     print("please enter a whole number between 1 and 10")
     # Ask for input
     user_balance = int(input("How much do you want to play with $"))
print(f"you are playing with ${user_balance}")

