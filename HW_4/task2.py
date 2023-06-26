# Задача 2

# Напишите функцию для транспонирования матрицы

def transpose(matrix):
    # return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    return [list(row) for row in zip(*matrix)]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))