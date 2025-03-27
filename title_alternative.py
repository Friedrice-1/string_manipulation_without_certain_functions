# ask user to input a statement
user_input = input("Please enter a statement: ")
# check if characters are in alphabet
title_case_user_input = ""
new_word = True
for char in user_input:
    if char.isalpha():
# check if it is a new word
# uppercase the first letter and lowercase letters after
        if new_word:
            title_case_user_input += chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        else:
            title_case_user_input += chr(ord(char) + 32) if 'A' <= char <= 'Z' else char
        new_word = False
    else:
        title_case_user_input += char
        new_word = True
# print output
print(title_case_user_input)