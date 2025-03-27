# ask user to input a statement
user_input = input("Please enter a statement: ")
# check if characters are in alphabet
title_case_user_input = ""
new_word = True
for char in user_input:
    if char.isalpha():
# check if it is a new word
        if new_word:
            print("its a new word")
        new_word = False
    else:
        new_word = True
# uppercase the first letter and lowercase letters after
# print output