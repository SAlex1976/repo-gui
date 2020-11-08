# Вычисление суммы чисел n + nn + nnn
number = input('Введите число:')
print(f'{number} + {number + number} + {number + number + number} = {int(number) + int(number * 2) + int(number * 3)}')