# ask user to input a statement
user_input = input("Please enter a statement: ")
# checks statement if it is all in uppercase
# prints result
if user_input.upper().lstrip() == user_input.lstrip():
    print("Characters are in uppercase")
else:
    print("Characters are not in uppercase")