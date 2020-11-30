# Task 2 Сalculating the total tissue consumption
from abc import ABC, abstractmethod
class Cloth:
    def __init__(self, user_data):
        self.user_data = user_data
    @abstractmethod
    def calc(self):
        pass
class Coat(Cloth):
    @property
    def calc(self):
        return round((self.user_data / 6.5) + 0.5)
class Costume(Cloth):
    @property
    def calc(self):
        return round(self.user_data * 2 + 0.3)
coat = Coat(45)
costume = Costume(170)
print(coat.calc)
print(costume.calc)
print(coat.calc + costume.calc)