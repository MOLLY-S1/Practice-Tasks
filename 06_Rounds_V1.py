""" V1 Component 4 Looping and Game mechanics
based on the token generator but hardwired to only allocate donkeys
Gives the user feedback about the number of rounds and maintains balance
Test amount set to $5
"""

import random

# Main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

# Testing loop to generate 5 tokens
while play_again != "x":
    rounds_played += 1  # keep track of rounds
    number = random.randint(6, 36) #can only be a donkey


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
        play_again = input("\n Do you want to play again?\n <enter> to play"
                           "again or 'X' to exit").lower()
    print()

print("Thanks for playing")
print(f"You started with ${TEST_AMOUNT:.2f}")
print(f"and leave with ${balance:.2f}")
print("Goodbye")
