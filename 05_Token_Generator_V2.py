""" Component 3 random token generator V2
generates random token choice in random order and will calculate the user balance
"""
import random
tokens = ["Unicorn", "Horse", "Donkey", "Zebra"]
balance = 100
# Testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')


    if token == 'Unicorn':
        balance += 4
    elif token == 'Donkey':
        balance -= 1
    else:
        balance -= .50

    print(f"\nToken:{token}, Balance:${balance}")
