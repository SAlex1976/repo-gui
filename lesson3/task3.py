# Task 3 Sum of greatest numbers
def my_func():
    try:
        num_1, num_2, num_3 = (int(i) for i in input('Введите 3 числа через пробел: ').split())
        my_list = [num_1, num_2, num_3]
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return 'Check number'

print('Сумма наибольших чисел равна: ', my_func())