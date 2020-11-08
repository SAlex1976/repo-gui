# Определение рентабельности
proceed = float(input('Сумма выручки: '))
cost = float(input('Сумма издержек: '))
profit = proceed - cost
if profit > 0:
    print('Прибыль организации:', profit)
    print('Рентабельность организации:', profit / proceed)
    people = int(input('Количество сотрудников в организации: '))
    print(f'Прибыль на одного сотрудника: {profit / people:.2f}')
elif profit < 0:
    print('Убыток организации:', profit)
else:
    print('Организация работает в 0')