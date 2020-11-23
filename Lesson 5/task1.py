# Task 1 Сreating a file with user data
user_line = 0
with open('task1.txt', 'w') as f:
    while user_line != '':
        user_line = input('Enter the string: ')
        f.write(user_line + '\n')