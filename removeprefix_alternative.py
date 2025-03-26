# ask user to input a word
user_input = input("Please enter an input: ")
# ask user the prefix to remove
prefix = input("Enter a prefix to remove: ")

# remove prefix
if user_input.startswith(prefix):
    new_user_input = user_input[len(prefix):]

# print result
print(new_user_input)