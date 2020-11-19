# Task 7
# Пользовался разбором ДЗ
from math import factorial
from itertools import count


def fibo_gen():
    for el in count(1):  # бесконечный цикл, который начинается с 1
        yield factorial(el)


x = 1
for i in fibo_gen():
    print('Factorial {} - {}'.format(x, i))
    if x == 15:
        break
    x += 1
