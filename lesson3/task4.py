# Task 4 Exponentiation
# Способ 1
def my_func(x, y):
    try:
        x, y = float(x), int(y)
    except TypeError:
        return 'TypeError'
    return x ** y

# Способ 2
def my_pow_func(x, y):
    try:
        x, y = float(x), int(y)
        if y >= 0:
            return x ** y
        res = x
        for i in range(abs(y) - 1):
            res *= x  # res = res * x
        return 1 / res
    except ValueError:
        return 'ValueError'

x, y = ((i) for i in input('Введите положительное число x и целое отрицательное число y через пробел: ').split())
print('Первый способ', my_func(x, y))
print('Второй способ', my_pow_func(x, y))