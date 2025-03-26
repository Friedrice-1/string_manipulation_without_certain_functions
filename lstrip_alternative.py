# get input from user

user_input = input("Please enter a statement: ")

# find the first non space character
index = 0
while index < len(user_input) and user_input[index] == ' ':
    index += 1
    
user_input = user_input[index:]

# create the new string without the spaces at the left side
# print output