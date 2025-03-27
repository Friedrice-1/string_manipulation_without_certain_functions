# ask user to input a statement
user_input = input("Please enter a statement: ")
# check if characters are in alphabet
for char in user_input:
    if char.isalpha():
        print("Character is in alphabet")
# check if it is a new word
# uppercase the first letter and lowercase letters after
# print output