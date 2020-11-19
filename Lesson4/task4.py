# Task 4 Non-repeating numbers output
num_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list = [el for el in num_list if num_list.count(el) == 1]
print(num_list,"\n", my_list)