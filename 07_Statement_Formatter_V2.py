""" Component 5 statement formatter v2
Changing V1 to a function
"""

def formatter(symbol, text):
    sides = symbol * 5
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine
text1 = input("Enter the statement you want format: ")
symbol1 = input("Enter the decoration you want to use: ")
print()
print(formatter(symbol1, text1))
