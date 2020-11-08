# Вычисление дней для достижения спортивного результата
min_distance = int(input('Стартовый результат: '))
max_distance = int(input('Финальный результат: '))
day = 1
if min_distance > max_distance:
    print('Введены неверные данные')
else:
    while min_distance < max_distance:
        min_distance = min_distance + min_distance * 0.1
        day = day + 1
print('Спортсмен добьется результата за {} дней'.format(day))