# Перевод секунд в часы и минуты
time = int(input('Введите время в секундах:'))
hour = time // 3600
minute = (time // 60) - (hour * 60)
second = time % 60
print(f'{hour:02}h:{minute:02}m:{second:02}s')