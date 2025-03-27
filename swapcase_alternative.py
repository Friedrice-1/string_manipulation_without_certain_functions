# ask user to input a statement
user_input = input("Please enter a statement: ")
# format the statement without the use of swapcase
swapcase_user_input = ""
for char in user_input:
    if 'A' <= char <= 'Z':
        swapcase_user_input += chr(ord(char) + 32)
    elif 'a' <= char <= 'z':
        swapcase_user_input += chr(ord(char) - 32)
    else:
        swapcase_user_input += char
# print output
print(swapcase_user_input)