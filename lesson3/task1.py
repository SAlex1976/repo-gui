# Task 1 Division of numbers
def my_div(*args):
    try:
        num_1, num_2 = (float(i) for i in input('Введите да числа через пробел: ').split())
        ans = num_1 / num_2
    except ValueError:
        return 'Ошибка - введено не число'
    except ZeroDivisionError:
        return 'Ошибка - деление на ноль.'
    return ans

print('X / Y = ', my_div())