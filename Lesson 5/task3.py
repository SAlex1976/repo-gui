# Task 3 Calculating the average income of employees
with open('task3.txt') as f:
    bonus_list = []
    line = f.readlines()
    for num_line in line:
        name, bonus = num_line.split('-')
        bonus_list.append(int(bonus))
        if int(bonus) < 20000:
            print('\nSalary less than 20,000: ', name)
    print('\nAverage salary:', '%.2f' % (sum(bonus_list) / len(bonus_list)))