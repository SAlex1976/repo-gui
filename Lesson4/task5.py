# Task 5 Output of the product of list items
from functools import reduce

def mum_list(num1, num2):
    return num1 * num2

my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(mum_list, my_list))