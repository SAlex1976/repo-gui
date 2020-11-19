# Task 2 List the maximum values
num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('List: ', num_list)
new_list = [num for i, num in enumerate(num_list) if i > 0 and num_list[i - 1] < num_list[i]]
print('New list', new_list)