# Task 6 Dictionary containing the name of the subject and the total number of classes on it
my_dict = dict()
with open('task6.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for dict_line in lines:
        split_list = dict_line.split()
        lesson = split_list[0]
        sum_hour = sum([int(i[:i.find('(')]) for i in split_list[1:] if '(' in i])
        my_dict[lesson[:-1]] = sum_hour
print(my_dict)