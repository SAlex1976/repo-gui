# Task 5 Count the sum of the numbers in the file and display it on the screen
with open('task5.txt', 'w') as f:
    user_num = input('Enter whole numbers separated by a space: ')
    f.write(user_num)
    user_num = map(int, user_num.split())
    sum_num = sum(user_num)
    print('Sum of numbers:', sum_num)
    f.write("\n" + str(sum_num))