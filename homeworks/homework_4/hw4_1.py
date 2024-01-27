"""
Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix,
и возвращает транспонированную матрицу.
Пример использования На входе:
matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
transposed_matrix = transpose(matrix)
На выходе:
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def transpose(matrix):
    return list([x for x in elem] for elem in list(zip(*matrix)))


transposed_matrix = transpose(matrix)
print(transposed_matrix)

"""решение в примере"""
# def transpose(matrix):
#     # определяем количество строк и столбцов в матрице
#     rows = len(matrix)
#     cols = len(matrix[0])
#
#     # создаем новую матрицу с размерами, поменянными местами
#     transposed = [[0 for row in range(rows)] for col in range(cols)]
#
#     # заполняем новую матрицу значениями из старой матрицы
#     for row in range(rows):
#         for col in range(cols):
#             transposed[col][row] = matrix[row][col]
#
#     return transposed

