""" Component 3 random token generator V3
generates random token choice in random order and will calculate the user balance
chance of a unicorn will become 10% all else will have a 30% chance
"""
import random
tokens = ["Unicorn",
          "Zebra", "Zebra", "Zebra",
          "Donkey", "Donkey", "Donkey",
          "Horse", "Horse", "Horse"]

STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 100 tokens
for item in range(100):
    token = random.choice(tokens)

    if token == 'Unicorn':
        balance += 4
    elif token == 'Donkey':
        balance -= 1
    else:
        balance -= .50

    print(f"Token:{token} Balance:${balance:.2f}")


print(f"\nstarting balance:{STARTING_BALANCE:.2f}")
print(f"final balance:{balance:.2f}")
