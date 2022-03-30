# More Efficiant testing with loops



# Functions

def yes_no(question_text):
    while True:

        # Ask user if they have played before
        answer = input(question_text).lower()


        # If they say yes, output 'Program Continues'
        if answer == 'yes' or answer == 'y':
            answer == 'Yes'
            return answer


        # If they say no, output 'Display instructions'
        elif answer == 'no' or answer == 'n':
            answer == 'No'
            return answer


        # Otherwise - show error
        else:
            print("please enter 'yes' or 'no'")



# Main routine

show_instructions = yes_no("have you played this game before? :")
print(f"you entered '{show_instructions}'")
print()
having_fun = yes_no("are you having fun? :")
print(f"you entered '{having_fun}'")

