# Task 3 Worker
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'
    def get_total_income(self):
        return self._income_wage + self._income_bonus

user_data = input('Введите Имя, Фамилию, должность. оклад и премию через пробел: ')
user_list = user_data.split()
pos = Position(user_list[0], user_list[1], user_list[2], {"wage": float(user_list[3]), "bonus": float(user_list[4])})
print('Full name:', pos.get_full_name(), '\nIncome:', pos.get_total_income())