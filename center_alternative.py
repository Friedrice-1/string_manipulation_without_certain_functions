# ask user to enter a statement
user_input = input("Enter a statement: ")
# ask user to enter the width to adjust
width = int(input("Enter the total width: "))
# adjust the statement based on the width entered on both sides
if len(user_input) < width:
    total_spaces = width - len(user_input)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    user_input = " " * left_spaces + user_input + " " * right_spaces
# print output
print(f"'{user_input}'")