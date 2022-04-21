"""LU Base Component V2 based on V1
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


# Function to generate a random token
def generate_token(balance):

    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1  # keep track of rounds
        number = random.randint(1, 100)  # Can be any token

        # Adjust balance according to the token
        if 1 <= number <= 5:
            token = "Unicorn"
            balance += 4

        elif 6 <= number <= 36:
            token = "Donkey"
            balance -= 1

        else:
             # If even then token is Zebra
            if number % 2 == 0:
                token = "Zebra"
                balance -= .50

            # Otherwise, it will be a Horse
            else:
                token = "Horse"
                balance -= .50

        # Output
        print(f"Round {rounds_played}. Token: {token}, Balance: ${balance:.2f}")
        if balance < 1:
            print("\nSorry but you are out of money")
            play_again = "x"
        else:
            play_again = input("\n Do you want to play again?\n <enter> to play "
                               "again or 'X' to exit").lower()
        print()
    return balance


# Main routine go here
played_before = yes_no("have you played this game before? :")
if played_before == "No":
    instructions()

starting_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print("Goodbye")


