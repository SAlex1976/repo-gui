#Task 3 Cell
# Пользовался разбором ДЗ
class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return str(self.nums + other.nums) + ' Sum of cell'

    def __sub__(self, other):
        if self.nums - other.nums > 0 :
            return self.nums - other.nums

    def __mul__(self, other):
        return str(self.nums * other.nums)

    def __truediv__(self, other):
        return str(round(self.nums / other.nums))

cell_1 = Cell(14)
cell_2 = Cell(24)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2.make_order(10))