# Task 6
# An iterator that generates integers
from itertools import count, cycle

for i in count(int(input('Enter start number: '))):
    if i < 10:
        print(i)
    else:
        break

# An iterator that iterates over the elements of a list
itr = cycle([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])
brk = ''
while brk != 'q':
    print(next(itr))
    brk = input()
