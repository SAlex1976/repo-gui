# Task 1 Matrix
class Matrix:
    def __init__(self, user_data):
       self.data = user_data
    def __str__(self):
        return '\n'.join([' '.join([str(el) for el in line]) for line in self.data])
    def __add__(self, other):
        result = ''
        for line_1, line_2 in zip(self.data, other.data):
                sum_line = [x + y for x, y in zip(line_1, line_2)]
                result += ' '.join([str(i) for i in sum_line]) + '\n'
        return result
matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[7, 8, 6], [3, 4, 5], [1, 0, 2]])
print('Matrix 1')
print(matrix_1, '\n')
print('Matrix 2')
print(matrix_2, '\n')
print("Matrix 1 + Matrix 2")
print(matrix_1 + matrix_2)