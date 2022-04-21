""" Component 3 random token generator V4
calculate percentages to ensure the house has an advantage
5% Unicorns, 30% Donkeys and all else 65%
"""
import random


STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 100 tokens
for item in range(10):
    number = random.randint(1, 100)
# Add $4 for Unicorns
    if  1<= number <=5:
        token = "Unicorn"
        balance += 4
# Lose $1 for Donkeys
    elif 6<= number <= 36:
        token = "Donkey"
        balance -= 1

# Lose $0.5 for all else
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
    print(f"Token:{token}, Balance:${balance:.2f}")

print()
print(f"\nStarting Balance:${STARTING_BALANCE:.2f}")
print(f"Final Balance:${balance:.2f}")
