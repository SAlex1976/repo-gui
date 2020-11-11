# Task_6 (Пользовался разбором ДЗ)
# Data structure products
goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
user_choice = 1
while user_choice != 'Q' or user_choice != 'q':
    user_choice = input('Для выхода нажмите - Q, для продолжения нажмите любую клавишу: ')
    num += 1
    for f in features.keys():
        user_data = input(f'{f}: ')
        features[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analitics[f].append(features[f])
    goods.append((num, features.copy()))
    print('Текущая аналитика по товарам:\n')
    for key, value in analitics.items():
        print(key, value)