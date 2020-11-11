# Task_2
# Swapping values of adjacent elements
user_list = list(input('Enter text: '))
print(user_list, 'List before changes')
for i in range(1, len(user_list), 2):
    user_list[i - 1], user_list[i] = user_list[i], user_list[i - 1]
print(user_list, 'List after changes')