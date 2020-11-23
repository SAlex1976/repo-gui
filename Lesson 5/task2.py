# Task 2 Counting the number of lines, the number of words in each line
with open('task2.txt') as f:
    line = f.readlines()
print('Number of lines:', len(line))
for num_line, wrds in enumerate(line, start=1):
    print('In line {} - {} words'.format(num_line, len(wrds.split())))