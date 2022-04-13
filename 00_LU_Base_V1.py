"""LU Base Component
All components added after creation and testing
"""
# Functions go here...

# Yes/No Checker
def yes_no(question_text):
    while True:

        # Ask user if they have played before
        answer = input(question_text).lower()


        # If they say yes, output 'Program Continues'
        if answer == 'yes' or answer == 'y':
            answer = 'Yes'
            return answer


        # If they say no, output 'Display instructions'
        elif answer == 'no' or answer == 'n':
            answer = 'No'
            return answer


        # Otherwise - show error
        else:
            print("please enter 'yes' or 'no'\n")

# Function to display instructions
def instructions():
    print("*** How To Play ***")
    print()
    print("The rules of the game will go here")
    print()


#Number checking function
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


played_before = yes_no("have you played this game before? :")
if played_before == "No":
    instructions()

user_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")

