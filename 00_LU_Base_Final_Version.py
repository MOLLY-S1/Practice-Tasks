"""LU Base Component V3 based on V2
All components added after creation and testing
"""

import random


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
    print("\nUnicorns give you $4, Donkeys make you lose $1 and both horses and zebras make you lose $0.50\n"
          "Press <enter> to continue playing or 'X' to stop at the end of each round\n"
          "The game will continue until you press 'X' or you run out of money to play with")
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


# Function to generate a random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1  # keep track of rounds
        print(formatter(".", f"Round {rounds_played}"))
        print()
        number = random.randint(1, 100)  # Can be any token

        # Adjust balance according to the token
        if 1 <= number <= 5:
            balance += 4
            print(formatter("*", "CONGRATULATIONS YOU GOT A UNICORN"))
            print()

        elif 6 <= number <= 36:
            balance -= 1
            print(formatter("D", "You got a DONKEY"))
            print()

        else:
             # If even then token is Zebra
            if number % 2 == 0:
                balance -= .50
                print(formatter("Z", "You got a ZEBRA"))
                print()

            # Otherwise, it will be a Horse
            else:
                balance -= .50
                print(formatter("H", " You got a HORSE"))
                print()

        # Output
        print(f"Round {rounds_played}. Your Balance is: ${balance:.2f}")
        if balance < 1:
            print("\nSorry but you are out of money")
            play_again = "x"
        else:
            play_again = input("\n Do you want to play again?\n <enter> to play "
                               "again or 'X' to exit").lower()
        print()
    return balance


# function to format text output
def formatter(symbol, text):
    sides = symbol * 5
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine go here
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()

played_before = yes_no("have you played this game before? :")
if played_before == "No":
    instructions()

starting_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print(formatter("=", "Goodbye"))


