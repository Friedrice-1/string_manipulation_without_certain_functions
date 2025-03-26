# ask user to input a statement
user_input = input("Please enter an input: ")
# ask user to check what the statement ends with
ends_with = input("Enter to check if the statements ends with it: ")
# checks if it ends with the input entered
# print output
if ends_with == user_input[-len(ends_with):]:
    print(f"It ends with {ends_with}")
else:
    print(f"It does not end with {ends_with}")