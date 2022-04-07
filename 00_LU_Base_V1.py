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
            print("please enter 'yes' or 'no'")

# Function to display instructions
def instructions():
    print("*** How To Play ***")
    print()
    print("The rules of the game will go here")
    print()
    print("Program Continues")
    print()

# Main routine

played_before = yes_no("have you played this game before? :")
if played_before == "No":
    instructions()
else:
    print("Program Continues")

