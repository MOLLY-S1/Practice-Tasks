""" Component 5 statement formatter V3
Based off V2
"""


# function to format text output
def formatter(symbol, text):
    sides = symbol * 5
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
print(formatter("*", "CONGRATULATIONS YOU GOT A UNICORN"))
print()
print(formatter("=", "Goodbye"))
