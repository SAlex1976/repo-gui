# Task 2 Asphalt mass calculation
class Road():
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
    def calc(self):
        mass = self._lenght * self._width * 0.025 * 5
        return mass
user_data = input('Введите длину и ширину дороги в метрах через пробел: ')
words = user_data.split()
road = Road(float(words[0]), float(words[1]))
print('Необходимо {}'.format(road.calc()), 'тонн')