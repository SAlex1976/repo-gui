# Определение максимальной цифры в числе
user_namber = int(input('Введите целое положительное число: '))
n = user_namber
n_max = 0
while n > 0:
    n_last = n % 10
    if n_last > n_max:
        n_max = n_last
    n = n // 10
print('Максимальная цифра в числе:', n_max)