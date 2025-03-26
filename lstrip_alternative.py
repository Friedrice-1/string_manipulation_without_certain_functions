# get input from user

user_input = input("Please enter a statement: ")

# find the first non space character
index = 0
while index < len(user_input) and user_input[index] == ' ':
    index += 1

# create the new string without the spaces at the left side
user_input = user_input[index:]
# print output
print(user_input)