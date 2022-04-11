""" Component 3 random token generator V1
generates random token choice in random order
"""
import random
tokens = ["Unicorn", "Horse", "Donkey", "Zebra"]

# Testing loop to generate 20 tokens
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')
