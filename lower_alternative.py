# ask user to input a statement
user_input = input("Please enter a statement: ")
# convert each character from string to lowercase
lowercase_user_input = ""
for char in user_input:
    if 'A' <= char <= 'Z':
        lowercase_user_input += chr(ord(char) + 32)
    else:
        lowercase_user_input += char
# print output