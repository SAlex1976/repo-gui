# Task_4
# Output a numbered list
user_text = input('Enter words separated by spaces: ')
user_list = user_text.split()
for i, num_list in enumerate(user_list):
    print(i + 1, num_list[:10])