# 2) Создайте класс Матрица. Добавьте методы для:
# - вывода на печать,
# сравнения,
# сложения,
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * self.cols for _ in range(self.rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __eq__(self, other):
        return isinstance(other, Matrix) and (self.rows, self.cols) == (other.rows, other.cols)

    def __add__(self, other):
        if isinstance(other, Matrix) and (self.rows, self.cols) == (other.rows, other.cols):
            result = Matrix(self.rows, self.cols)
            result.matrix = [[self.matrix[row][col] + other.matrix[row][col]
                for col in range(self.cols)]
                for row in range(self.rows)]
            return result


m1 = Matrix(2, 3)
m1.matrix = [[1, 2, 3], [4, 5, 6]]
print(m1)

m2 = Matrix(2, 3)
m2.matrix = [[1, 2, 3], [4, 5, 6]]
print(m2)

print(m1 == m2)

m3 = m1 + m2
print(m3)