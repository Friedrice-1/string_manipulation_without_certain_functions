# ask user to input a statement
user_input = input("Please enter a statement: ")
# convert statement to lower case
for char in user_input:
    if 'a' <= char <= 'z':
        capitalize_user_input += chr(ord(char) + 32)
    else:
        capitalize_user_input += char
# capitalize the first letter
for char in user_input[1:]:
    if 'A' <= char <= 'Z':  
        capitalize_user_input += chr(ord(char) + 32)  
    else:  
        capitalize_user_input += char
# print output
print(capitalize_user_input)