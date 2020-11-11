# Task_3
# Determining the time of year by month

# Branching
month = 0
print('Solution through the branching')
while month < 1 or month > 12:
    month = int(input('Enter month: '))
if month > 11 or month < 3:
    print('Winter')
elif month < 6 and month > 2:
    print('Spring')
elif month < 9 and month > 5:
    print('Summer')
else:
    print('Autumn')

# List
month_list = ['Winter',
              'Winter',
              'Spring',
              'Spring',
              'Spring',
              'Summer',
              'Summer',
              'Summer',
              'Autumn',
              'Autumn',
              'Autumn',
              'Winter']
month_num = 0
print('Solution through the list')
while month_num < 1 or month_num > 12:
    month_num = int(input('Enter month: '))
print(month_list[month_num - 1])

# Dict
month_dict = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter',
}
month_num = 0
print('Solution through the dictionary')
while month_num < 1 or month_num > 12:
    month_num = int(input('Enter month: '))
print(month_dict[month_num])