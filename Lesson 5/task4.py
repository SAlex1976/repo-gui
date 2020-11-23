# Task 4 Replace data
with open('task4.txt', encoding='utf-8') as f:
    lines = f.readlines()
with open('task4_new.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        if '1' in line:
            f.write(line.replace('One', 'Один'))
        elif '2' in line:
            f.write(line.replace('Two', 'Два'))
        elif '3' in line:
            f.write(line.replace('Three', 'Три'))
        elif '4' in line:
            f.write(line.replace('Four', 'Четыре'))