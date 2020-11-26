# Task 5 Сhancellery
class Stationery:
    def __init__(self, title):
        self.title = title
    print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(self.title, 'пишет')

class Pencil(Stationery):
    def draw(self):
        print(self.title, 'чертит')

class Handle(Stationery):
    def draw(self):
        print(self.title, 'рисует')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()