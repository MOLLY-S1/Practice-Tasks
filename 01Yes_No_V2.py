# More Efficiant testing with loops

show_instructions = ""
while show_instructions != 'x':

    # Ask user if they have played before
    show_intructions = input("have you played before? :").lower()


    # If they say yes, output 'Program Continues'
    if show_intructions == 'yes' or show_intructions == 'y':
        print("program continues")


    # If they say no, output 'Display instructions'
    elif show_intructions == 'no' or show_intructions == 'n':
        print('show instructions')


    # Otherwise - show error
    else:
        print("please enter 'yes' or 'no'")

    print(f"you entered '{show_intructions}'")
