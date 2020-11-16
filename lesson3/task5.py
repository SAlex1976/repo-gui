# Task 5 Displaying the sum of entered numbers
def summary():
    result = 0
    i = True
    while i == True:
        res_line = 0
        if result != 0: print("Сумма введенных чисел: ", result)
        user_num = input('Enter numbers or q to exit: ').split()
        for num in user_num:
            if 'q' in num:
                i = False
                break
            res_line += int(num)
        result += res_line
    return result

print('Общая сумма введенных чисел: ', summary())