""" Component 2 (How much) V4
Now a function
"""

def num_check(question, low, high):
     error = "That was not a valid input\n" \
             "Please enter a whole number between {} and {}\n".format(low, high)

     while True:
          try:
               resonse = int(input(question))
               if low <= resonse <= high:
                    return resonse
               else:
                    print(error)

          except ValueError:
               print(error)

#Main Routine

user_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")
