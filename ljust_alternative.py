# ask user to enter a statement
user_input = input("Enter a string: ")
# ask user to enter width to adjust
width = int(input("Enter the total width: "))
# adjust the statement based on the width entered
if len(user_input) < width:
    user_input = user_input + " " * (width - len(user_input))
# print output
print(f"Statement working same as ljust function: '{user_input}'")